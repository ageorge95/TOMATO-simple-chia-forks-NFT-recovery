from argparse import ArgumentParser
from logging import getLogger
import os,\
    sys
from back_end import Tomato
from config import assets
from base import configure_logger
from logging import getLogger

parser = ArgumentParser(description='CLI: TOMATO-simple-chia-forks-NFT-recovery |'
                                    ' ' + open(os.path.join(os.path.dirname(__file__),'version.txt'), 'r').read())

parser.add_argument('-a',
                    '--asset',
                    type=str,
                    help=f"The asset for which you want to recover the rewards."
                         f" Can be one of the following: { '|'.join(coin for coin in assets.keys()) }")

parser.add_argument('-d',
                    '--delayedPH',
                    type=str,
                    help='The delayed ph, where the rewards will be returned.'
                         ' Usually the 3rd address (ph) of the mnemonic that farmed the block.')

parser.add_argument('-l',
                    '--launcher',
                    type=str,
                    help='The launcher ID. To be taken from chia NOT from the chia forks.')

parser.add_argument('-c',
                    '--contract',
                    help='The contract encoded in the NFT plots. To be taken from chia NOT from the chia forks.')

if __name__ == '__main__':

    os.system("color") # enable color in the console

    args = parser.parse_args()

    configure_logger()
    _log = getLogger()

    # check for valid asset selection
    if args.asset not in assets.keys():
        _log.error(f" { args.asset } is not present in config.py. Add it there and try again.")
        raise Exception

    tomato = Tomato(delayedPH=args.delayedPH,
                    launcher=args.launcher,
                    contract=args.contract,
                    asset=args.asset)

    tomato.search_and_recover()