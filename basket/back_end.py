from chia.util.ints import uint64
from chia.util.byte_types import hexstr_to_bytes
from chia.util.bech32m import decode_puzzle_hash
from chia.types.blockchain_format.program import Program
from chia.types.blockchain_format.serialized_program import SerializedProgram
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.pools.pool_puzzles import SINGLETON_MOD_HASH,\
    create_p2_singleton_puzzle
from basket.config import assets
import requests
from basket.base import (db_wrapper_selector,
                         dummy_aggregated_sig)
from logging import getLogger
from traceback import format_exc
from yaml import safe_load
from os import path

requests.packages.urllib3.disable_warnings()

class Tomato():
    def __init__(self,
                 delayedPH,
                 launcher,
                 contract,
                 asset,
                 delay = 604800 # 7 days
                 ):

        self._log = getLogger()

        self.delayedPH_hex = delayedPH
        self.launcher_hex = launcher
        self.contract = contract
        self.asset = asset
        self.delay = delay

        self.delayedPH_bytes: bytes32 = bytes32(hexstr_to_bytes(self.delayedPH_hex))
        self.launcher_bytes: bytes32 = bytes32(hexstr_to_bytes(self.launcher_hex))
        self.contract_bytes: bytes32 = decode_puzzle_hash(self.contract)
        self.contract_hex: str = self.contract_bytes.hex()

        self.puzzle = create_p2_singleton_puzzle(SINGLETON_MOD_HASH,
                                                 self.launcher_bytes,
                                                 self.delay,
                                                 self.delayedPH_bytes)

        try:
            db_filepath = assets[self.asset]['db_filepath']
            db_ver = 0
            if 'v1' in path.basename(db_filepath).lower():
                db_ver = 1
            if 'v2' in path.basename(db_filepath).lower():
                db_ver = 2
            self.db_wrapper = db_wrapper_selector(db_ver)()
            if not self.db_wrapper:
                self._log.error('Incompatible DB version !')
                raise Exception
            self.db_wrapper.connect_to_db(
                db_filepath=assets[self.asset]['db_filepath']
            )

            with open(path.join(assets[self.asset]['db_filepath'], '../../config/config.yaml'), 'r') as yaml_config_handle:
                yaml_config = safe_load(yaml_config_handle)
            self.full_node_RPC_port = yaml_config['full_node']['rpc_port']

        except:
            self._log.error(f"Failed to perform initial steps:\n{ format_exc(chain=False) }")

        self.check_correct_delayedPH()

    def check_correct_delayedPH(self):
        if not self.contract_bytes == self.puzzle.get_tree_hash():
            self._log.error('Your delayedPH or your launcher is wrong. Please read the instructions on github'
                            ' (https://github.com/ageorge95/TOMATO-simple-chia-forks-NFT-recovery) and try again.')
            raise Exception

    def search_and_recover(self):
        try:
            # search for coins that still need more time to be recovered
            self._log.info('Searching for unqualified coins, please wait ...')
            coins = self.db_wrapper.get_unqualified_coins(
                delay=self.delay,
                contract_hex=self.contract_hex
            )
            unqualified_len = len(coins)
            unqualified_amount = sum([int.from_bytes(x[1], byteorder='big', signed=False)/assets[self.asset]['denominator'] for x in coins])
            self._log.info(f"There are { unqualified_len } unqualified coins (that cannot be recovered YET), adding up to"
                           f" { unqualified_amount } { self.asset }.")

            # search for qualified coins
            self._log.info('Searching for qualified coins (that can be recovered), please wait ...')
            coins = self.db_wrapper.get_qualified_coins(
                delay=self.delay,
                contract_hex=self.contract_hex
            )

            qualified_len = len(coins)
            qualified_amount = sum([int.from_bytes(x[1], byteorder='big', signed=False)/assets[self.asset]['denominator'] for x in coins])
            self._log.info(f"There are { qualified_len } qualified coins, adding up to"
                           f" { qualified_amount } { self.asset }.")

            if not len(coins):
                self._log.info(f"$$Recovered 0 coins, with a value of 0 | { self.asset }$$")
            else:
                coin_solutions = []
                for coin in coins:
                    coin_parent: str = coin[0]
                    coin_amount: int = int.from_bytes(coin[1], byteorder='big', signed=False)

                    coin_solution_hex: str = bytes(SerializedProgram.from_program(
                        Program.to([uint64(coin_amount), 0])
                    )).hex()

                    coin_solutions.append({
                        'coin': {
                            'amount': coin_amount,
                            'parent_coin_info': '0x' + coin_parent,
                            'puzzle_hash': '0x' + self.contract_hex
                        },
                        'puzzle_reveal': '0x' + bytes(SerializedProgram.from_program(self.puzzle)).hex(),
                        'solution': '0x' + coin_solution_hex
                    })

                recovered_value = 0
                recovered_coins = 0

                ssl_crt = path.join(assets[self.asset]['db_filepath'], '../../config/ssl/full_node/private_full_node.crt')
                ssl_key = path.join(assets[self.asset]['db_filepath'], '../../config/ssl/full_node/private_full_node.key')

                for coin_solution_batch in [coin_solutions[x:x + 20] for x in range(0, len(coin_solutions), 20)]:
                    try:
                        coin_amount = sum([entry['coin']['amount']/assets[self.asset]['denominator'] for entry in coin_solution_batch])
                        self._log.info(f"Trying to recover a batch of { len(coin_solution_batch) } "
                                       f"coins adding up to  { coin_amount } { self.asset } ...")

                        # use the 2 known ways to describe the spend bundle
                        # in this way compatibility with all the forks should be assured
                        for variation in ['coin_spends', 'coin_solutions']:
                            self._log.info(f'Trying variation {variation} ...')
                            response = requests.post(
                                url=f'https://localhost:{ self.full_node_RPC_port }/push_tx',
                                cert=(ssl_crt,
                                      ssl_key),
                                verify=False,
                                json={
                                    'spend_bundle': {
                                        'aggregated_signature': dummy_aggregated_sig,
                                        variation: coin_solution_batch
                                    }
                                })
                            try:
                                response_json = response.json()
                            except:
                                response_json = {'success': False,
                                                 'reason': response.content}
                                self._log.error(f'Failed to convert the full node response to json. Reason:\n{format_exc(chain=False)}')
                            self._log.info(f"The full node responded with { response_json }")
                            if response_json['success']:
                                break

                        if not response_json['success']:
                            break
                        self._log.info('Recovery completed !')
                        recovered_value += coin_amount
                        recovered_coins += len(coin_solution_batch)

                    except:
                        self._log.error(f"Error found while trying to recover the coin !\n{ format_exc(chain=False) }")
                        recovered_value = -1
                        recovered_coins = -1
                self._log.info(f"$$Recovered { recovered_coins } coins, with a value of { recovered_value } | { self.asset }$$")

        except:
            self._log.error(f"Oh snap, an unknown error has occurred:\n{ format_exc(chain=False) }")