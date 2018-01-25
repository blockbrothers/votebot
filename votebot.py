import logging
import logging.config
import json
import os
from time import monotonic, sleep

from steem import Steem
from steem.utils import time_elapsed

import config


logging.config.dictConfig(config.LOGGING)
logger = logging.getLogger()


class VoteBot(object):

    def __init__(self, nodes, debug=False):
        self._debug = debug
        self._steemd = Steem(nodes=nodes, debug=debug, no_broadcast=debug, timeout=5)

    def run(self):
        logger.info("### Running Votebot ###")
        self.load_state()

        votes = []
        accounts = config.WATCHED_ACCOUNTS
        for account, params in accounts.items():
            weight = float(params.get('vote_weight', 100.0))
            max_votes = int(params.get('max_votes_per_day', 1))
            delay = int(params.get('delay', 1801))

            user_state = {
                'last_entry_id': -1,
                'previous_votes': [],
            }
            user_state.update(self._state.get(account, {}))
            logger.debug("user state for {}: {}".format(account, user_state))

            # Remove obsolete vote times from list
            now = monotonic()
            for idx, vote_time in enumerate(user_state['previous_votes']):
                if now - vote_time > config.DAY:
                    del user_state['previous_votes'][idx]

            post = None
            try:
                post = self.get_blogs(account)[0]
            except (TypeError, IndexError):
                pass

            if not post:
                logger.error("Failed to get post for account {}".format(account))
                continue

            if len(user_state['previous_votes']) >= max_votes:
                # Already cast maximum amount of votes for this user today
                continue

            entry_id = int(post.get('entry_id', -1))
            post = post.get('comment', {})
            created = post.get('created')
            permlink = post.get('permlink')
            if entry_id == -1 or not created or not permlink:
                # This should never happen, but just-in-case...
                continue
            if entry_id <= user_state['last_entry_id']:
                # Already processed this one.
                continue

            age = time_elapsed(created).total_seconds()
            if age > config.MAX_POST_AGE or age >= config.WEEK:
                # Mark post as already processed
                user_state['last_entry_id'] = entry_id
                continue
            elif age >= delay:
                self.vote(permlink, account, weight)
                user_state['last_entry_id'] = entry_id
                user_state['previous_votes'].append(now)
                sleep(3)    # can't vote more than once every 3 sec.

            self._state[account] = user_state
            self.save_state()

    def get_blogs(self, account):
        total_nodes = len(config.STEEM_RPC_NODES)
        retries = config.STEEMD_RETRIES
        failover_count = 0
        blogs = None
        while failover_count < total_nodes and blogs is None:
            while retries:
                try:
                    blogs = self._steemd.get_blog(account=account, entry_id=-1, limit=1)
                except:
                    logger.exception("Error retrieving blogs.")
                    blogs = None

                if blogs:
                    return blogs

                retries -= 1

            self._steemd.next_node()
            failover_count += 1

    def vote(self, permlink, author, weight):
        options = {
            'identifier': "@{author}/{permlink}".format(author=author, permlink=permlink),
            'weight': weight,
            'account': config.STEEM_USER,
        }
        try:
            self._steemd.commit.vote(**options)
        except:
            logger.exception("Error while voting on post \"{}\" by @{} at {}%".format(permlink, author, weight))
        else:
            logger.info("Voted on post \"{}\" by @{} at {}%".format(permlink, author, weight))

    def load_state(self):
        self._state = {}
        try:
            with open(config.TMP_FILE, mode='r+') as f:
                try:
                    self._state = json.load(f)
                except json.decoder.JSONDecodeError:
                    pass
        except FileNotFoundError:
            pass

    def save_state(self):
        with open(config.TMP_FILE, mode='w') as f:
            json.dump(self._state, f)


if __name__ == '__main__':
    os.environ['UNLOCK'] = str(config.WALLET_PASSWORD)
    try:
        votebot = VoteBot(nodes=config.STEEM_RPC_NODES, debug=config.DEBUG)
        votebot.run()
    except:
        logger.exception("Votebot failed!")
    finally:
        del os.environ['UNLOCK']
