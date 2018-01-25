import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TMP_FILE = os.path.join(BASE_DIR, '_tmp.json')


MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY


DEBUG = False


STEEM_USER = 'blockbrothers'
WALLET_PASSWORD = ''


WATCHED_ACCOUNTS = {
    'bennierex': {
        'weight': 100,
        'delay': 5 * MINUTE,
        'max_per_day': 2,
    },
    'eqko': {
        'weight': 100,
        'delay': 25 * MINUTE,
        'max_per_day': 2,
    },
    'exyle': {
        'weight': 100,
        'delay': 15 * MINUTE,
        'max_per_day': 2,
    },
    's3rg3': {
        'weight': 100,
        'delay': 35 * MINUTE,
        'max_per_day': 2,
    },
}


STEEM_RPC_NODES = [
    'https://api.steemit.com',                  # │ @steemit
    'https://steemd.minnowsupportproject.org',  # │ @followbtcnews
    'https://gtg.steem.house:8090',             # │ @gtg
    'https://steemd.pevo.science',              # │ @pharesim
    'https://rpc.buildteam.io',                 # │ @themarkymark
    'https://rpc.steemviz.com',                 # │ @ausbitbank
    'https://seed.bitcoiner.me',                # │ @bitcoiner
    #'https://steemd.privex.io',                 # │ @privex
    #'https://rpc.steemliberator.com',           # │ @netuoso
]


LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
        'rotating_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'default',
            'filename': os.path.expanduser('~/votebot.log'),
            'when': 'midnight',
            'interval': 1,
            'backupCount': 6,
            'utc': True,
        },
        # 'email': {
        #     'class': 'logging.handlers.SMTPHandler',
        #     'formatter': 'default',
        #     'level': 'INFO',
        #     'mailhost': ('localhost', 25),
        #     'fromaddr': '',
        #     'toaddrs': [''],
        #     'subject': '[VOTEBOT] Log message',
        # },
    },
    'formatters': {
        'brief': {
            'format': '%(message)s',
        },
        'default': {
            'format': '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'rotating_file'],
    },
}
