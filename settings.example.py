import os.path


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP_FILE = os.path.join(BASE_DIR, 'config', '_tmp.json')


MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY


DEBUG = False


STEEM_USER = ''         # set to the Steem account name (without the `@`) corresponding to the private key in the wallet.
WALLET_PASSWORD = ''    # set to your wallet password.


# Specify the accounts you'd like the bot to track.
WATCHED_ACCOUNTS = {
    # 'blockbrothers': {            # account name (without the `@`)
    #     'weight': 100.0,          # vote percentage                           [defaults to 100%]
    #     'delay': 5 * MINUTE,      # minimum delay before voting               [defaults to 30min]
    #     'max_per_day': 2,         # maximum votes cast per day (=24h period)  [defaults to 1]
    # },
}
MAX_POST_AGE = 3 * DAY              # Never vote on posts older than this (defines maximum delay that can be set in `WATCHED_ACCOUNTS`)


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
STEEMD_RETRIES = 3


LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
        # 'rotating_file': {
        #     'class': 'logging.handlers.TimedRotatingFileHandler',
        #     'formatter': 'default',
        #     'filename': os.path.expanduser('~/votebot.log'),
        #     'when': 'midnight',
        #     'interval': 1,
        #     'backupCount': 6,
        #     'utc': True,
        # },
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
            'format': '%(asctime)s %(levelname)-8s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'extended': {
            'format': '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console'],
    },
}
