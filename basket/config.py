from os import path

assets = {'XSEA': {'db_filepath': '{userdir}\\.sea\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                   'denominator': 1000000000000,
                   'friendly_name': 'seacoin'},
          'XCK': {'db_filepath': '{userdir}\\.chik\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                  'denominator': 1000000000000,
                  'friendly_name': 'chik'},
          'XTWO': {'db_filepath': '{userdir}\\.two\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                   'denominator': 1000000000000,
                   'friendly_name': 'two'},
          'BALL': {'db_filepath': '{userdir}\\.ball\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                   'denominator': 1000000000000,
                   'friendly_name': 'ball'},
          'XONE': {'db_filepath': '{userdir}\\.one\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                   'denominator': 100000000,
                   'friendly_name': 'one'},
          'KIK': {'db_filepath': '{userdir}\\.kiwi\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                   'denominator': 1000000,
                   'friendly_name': 'kiwi'},
          'GBTC': {'db_filepath': '{userdir}\\.greenbtc\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                   'denominator': 1000000000000,
                   'friendly_name': 'greenbtc'},
         'XCF': {'db_filepath': '{userdir}\\.coffee\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'coffee'},
          'MOC': {'db_filepath': '{userdir}\\.moon\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'moon'},
          'HCX': {'db_filepath': '{userdir}\\.chinilla\\vanillanet\\db\\blockchain_v2_vanillanet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'chinilla'},
          'XSE': {'db_filepath': '{userdir}\\.seno2\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'seno'},
          'XPT': {'db_filepath': '{userdir}\\.petroleum\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'petroleum'},
          'XGJ': {'db_filepath': '{userdir}\\.goji\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'goji'},
          'ECO': {'db_filepath': '{userdir}\\.ecostake\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'ecostake'},
          'XJK': {'db_filepath': '{userdir}\\.joker\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 100000000,
                 'friendly_name': 'joker'},
          'GL': {'db_filepath': '{userdir}\\.gold\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'gold'},
          'PROFIT': {'db_filepath': '{userdir}\\.profit\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'profit'},
          'LLC': {'db_filepath': '{userdir}\\.littlelambocoin\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000,
                 'friendly_name': 'littlelambocoin'},
          'BPX': {'db_filepath': '{userdir}\\.bpx\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'bpx'},
          'AEC': {'db_filepath': '{userdir}\\.aedge\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'aedge'},
         'APPLE': {'db_filepath': '{userdir}\\.apple\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                   'denominator': 1000000000000,
                   'friendly_name': 'apple'},
         'AVO': {'db_filepath': '{userdir}\\.avocado\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'avocado'},
         'CAC': {'db_filepath': '{userdir}\\.cactus\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'cactus'},
         'CANS': {'db_filepath': '{userdir}\\.cannabis\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                  'denominator': 1000000000000,
                  'friendly_name': 'cannabis'},
         'CGN': {'db_filepath': '{userdir}\\.chaingreen\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'chaingreen'},
         'COV': {'db_filepath': '{userdir}\\.covid\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'covid'},
         'GDOG': {'db_filepath': '{userdir}\\.greendoge\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                  'denominator': 1000000000000,
                  'friendly_name': 'greendoge'},
         'HDD': {'db_filepath': '{userdir}\\.hddcoin\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'hddcoin'},
         'LCH': {'db_filepath': '{userdir}\\.lotus\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'lotus'},
         'MELON': {'db_filepath': '{userdir}\\.melon\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                   'denominator': 1000000000,
                   'friendly_name': 'melon'},
         'MGA': {'db_filepath': '{userdir}\\.mogua\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'mogua'},
         'NCH': {'db_filepath': '{userdir}\\.chia\\ext9\\db\\blockchain_v1_ext9.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'n-chain_ext9'},
         'OZT': {'db_filepath': '{userdir}\\.goldcoin\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'Goldcoin'},
         'PEA': {'db_filepath': '{userdir}\\.peas\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'peas'},
         'PIPS': {'db_filepath': '{userdir}\\.pipscoin\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                  'denominator': 1000000000000,
                  'friendly_name': 'Pipscoin'},
         'ROLLS': {'db_filepath': '{userdir}\\.rolls\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                   'denominator': 1000000000000,
                   'friendly_name': 'rolls'},
         'SCM': {'db_filepath': '{userdir}\\.scam\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'Scamcoin'},
         'SIT': {'db_filepath': '{userdir}\\.sit\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'silicoin'},
         'SIX': {'db_filepath': '{userdir}\\.lucky\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'lucky'},
         'SOCK': {'db_filepath': '{userdir}\\.socks\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                  'denominator': 1000000000000,
                  'friendly_name': 'socks'},
         'SPARE': {'db_filepath': '{userdir}\\.spare\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                   'denominator': 1000000000000,
                   'friendly_name': 'spare'},
         'STAI': {'db_filepath': '{userdir}\\.stai\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                  'denominator': 1000000000,
                  'friendly_name': 'staicoin'},
         'STOR': {'db_filepath': '{userdir}\\.stor\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                  'denominator': 1000000000000,
                  'friendly_name': 'stor'},
         'TAD': {'db_filepath': '{userdir}\\.tad\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'tad'},
         'TRZ': {'db_filepath': '{userdir}\\.tranzact\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'tranzact'},
         'WHEAT': {'db_filepath': '{userdir}\\.wheat\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                   'denominator': 1000000000000,
                   'friendly_name': 'wheat'},
         'XBR': {'db_filepath': '{userdir}\\.beernetwork\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'Beer'},
         'XBT': {'db_filepath': '{userdir}\\.beet\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'Beet'},
         'XBTC': {'db_filepath': '{userdir}\\.btcgreen\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                  'denominator': 1000000000000,
                  'friendly_name': 'btcgreen'},
         'XCA': {'db_filepath': '{userdir}\\.xcha\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'xcha'},
         'XCC': {'db_filepath': '{userdir}\\.chives\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 100000000,
                 'friendly_name': 'chives'},
         'XCD': {'db_filepath': '{userdir}\\.cryptodoge\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000,
                 'friendly_name': 'cryptodoge'},
         'XCH': {'db_filepath': '{userdir}\\.chia\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'chia'},
         'XCR': {'db_filepath': '{userdir}\\.chiarose\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000,
                 'friendly_name': 'chiarose'},
         'XDG': {'db_filepath': '{userdir}\\.dogechia\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'dogechia'},
         'XETH': {'db_filepath': '{userdir}\\.ethgreen\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                  'denominator': 1000000000,
                  'friendly_name': 'ethgreen'},
         'XFK': {'db_filepath': '{userdir}\\.fork\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'fork'},
         'XFL': {'db_filepath': '{userdir}\\.flora\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'flora'},
         'XFX': {'db_filepath': '{userdir}\\.flax\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'flax'},
         'XKA': {'db_filepath': '{userdir}\\.kale\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'kale'},
         'XKJ': {'db_filepath': '{userdir}\\.kujenga\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'kujenga'},
         'XKM': {'db_filepath': '{userdir}\\.mint\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'mint'},
         'XKW': {'db_filepath': '{userdir}\\.kiwi\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'Kiwi'},
         'XMX': {'db_filepath': '{userdir}\\.melati\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'melati'},
         'XMZ': {'db_filepath': '{userdir}\\.maize\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'maize'},
         'XNT': {'db_filepath': '{userdir}\\.skynet\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'skynet'},
         'XOL': {'db_filepath': '{userdir}\\.olive\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'olive'},
         'XSC': {'db_filepath': '{userdir}\\.sector\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'sector'},
         'XSHIB': {'db_filepath': '{userdir}\\.shibgreen\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                   'denominator': 1000,
                   'friendly_name': 'shibgreen'},
         'XSLV': {'db_filepath': '{userdir}\\.salvia\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                  'denominator': 1000000000000,
                  'friendly_name': 'salvia'},
         'XTX': {'db_filepath': '{userdir}\\.taco\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'taco'},
         'XVM': {'db_filepath': '{userdir}\\.venidium\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                 'denominator': 1000000000000,
                 'friendly_name': 'venidium'}}