from sqlite3 import connect
from logging import basicConfig,\
    INFO, DEBUG, WARNING, ERROR, CRITICAL,\
    Formatter,\
    StreamHandler, FileHandler, Handler
from sys import stdout

dummy_aggregated_sig = '0xc00000000000000000000000000000000000000000000000000000000' \
                       '00000000000000000000000000000000000000000000000000000000000' \
                       '00000000000000000000000000000000000000000000000000000000000' \
                       '00000000000000000'

class db_wrapper_v1():
    def connect_to_db(self,
                      db_filepath):
        self._conn = connect(db_filepath)
        self._dbcursor = self._conn.cursor()

    def get_unqualified_coins(
            self,
            delay,
            contract_hex
    ):

        self._dbcursor.execute(
            f"SELECT coin_parent, amount "
            f"FROM coin_record "
            f"WHERE spent == 0 "
            f"AND timestamp > (strftime('%s', 'now') - { delay }) "
            f"AND puzzle_hash LIKE '{ contract_hex }' "
            f"ORDER BY timestamp DESC"
        )

        return self._dbcursor.fetchall()

    def get_qualified_coins(
            self,
            delay,
            contract_hex
    ):

        self._dbcursor.execute(
            f"SELECT coin_parent, amount "
            f"FROM coin_record "
            f"WHERE spent == 0 "
            f"AND timestamp <= (strftime('%s', 'now') - { delay }) "
            f"AND puzzle_hash LIKE '{ contract_hex }' "
            f"ORDER BY timestamp DESC"
        )

        return self._dbcursor.fetchall()

class db_wrapper_v2():
    def connect_to_db(self,
                      db_filepath):
        self._conn = connect(db_filepath)
        self._dbcursor = self._conn.cursor()

    def get_unqualified_coins(
            self,
            delay,
            contract_hex
    ):

        self._dbcursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(self._dbcursor.fetchall())

        self._dbcursor.execute(
            f"SELECT coin_parent, amount "
            f"FROM coin_record "
            f"WHERE spent_index == 0 "
            f"AND timestamp > (strftime('%s', 'now') - { delay }) "
            f"AND puzzle_hash LIKE ? "
            f"ORDER BY timestamp DESC",
            (bytes.fromhex(contract_hex),)
        )

        return [[entry[0].hex(),
                 entry[1]] for entry in self._dbcursor.fetchall()]

    def get_qualified_coins(
            self,
            delay,
            contract_hex
    ):

        self._dbcursor.execute(
            f"SELECT coin_parent, amount "
            f"FROM coin_record "
            f"WHERE spent_index == 0 "
            f"AND timestamp <= (strftime('%s', 'now') - { delay }) "
            f"AND puzzle_hash LIKE ? "
            f"ORDER BY timestamp DESC",
            (bytes.fromhex(contract_hex),)
        )

        return [[entry[0].hex(),
                 entry[1]] for entry in self._dbcursor.fetchall()]

def db_wrapper_selector(version: int):
    if version == 1:
        return db_wrapper_v1
    elif version == 2:
        return db_wrapper_v2
    else:
        return None

def configure_logger():
    class CustomFormatter(Formatter):
        grey = "\x1b[38;21m"
        yellow = "\x1b[33;21m"
        red = "\x1b[31;21m"
        bold_red = "\x1b[31;1m"
        reset = "\x1b[0m"
        format = '%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d -> %(name)s - %(funcName)s] ___ %(message)s'

        FORMATS = {
            DEBUG: grey + format + reset,
            INFO: grey + format + reset,
            WARNING: yellow + format + reset,
            ERROR: red + format + reset,
            CRITICAL: bold_red + format + reset
        }

        def format(self, record):
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = Formatter(log_fmt)
            return formatter.format(record)

    ch = StreamHandler(stream=stdout)
    ch.setLevel(DEBUG)
    ch.setFormatter(CustomFormatter())
    fh = FileHandler("runtime_log.log")
    fh.setLevel(DEBUG)
    fh.setFormatter(Formatter('%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d -> %(name)s - %(funcName)s] ___ %(message)s'))

    basicConfig(datefmt='%Y-%m-%d:%H:%M:%S',
                level=DEBUG,
                handlers=[
                    fh,
                    ch
                ])