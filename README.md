# A Steem votebot
A basic Steem votebot created by [@blockbrothers](https://steemit.com/@blockbrothers)

---

> #### Disclaimer
> Some of these instructions are specific to Ubuntu. Please adjust accordingly if you're using a differens OS.

## 1. Install docker if you haven't already
```bash
$ sudo apt update
$ sudo apt install curl git
$ curl https://get.docker.com | sh
$ sudo usermod -aG docker $(whoami)
```
**IMPORTANT: re-login to activate the changes.**

## 2. Install votebot & initial setup
```bash
$ mkdir -p ~/votebot/config && cd ~/votebot
$ docker pull blockbrothers/votebot:latest
$ docker run -v $(pwd)/config:/usr/src/votebot/config -d --name votebot -t votebot:latest
$ docker exec -ti votebot steempy addkey
```
Enter your private POSTING key:
```
Private Key (wif) [Enter to quit]:
```
Set a passphrase for the wallet:
```
Please provide a password for the new wallet
Passphrase:
Confirm Passphrase:
```
Then steempy will prompt you again for a Private Key. Just press [ENTER] to quit.

## 3. Configure votebot
```
nano ./config/settings.py
```
The most important settings are:
```python
STEEM_USER = ''         # set to the Steem account name (without the `@`) corresponding to the private key in the wallet.
WALLET_PASSWORD = ''    # set to your wallet password set in step 2.

# Specify the accounts you'd like the bot to track.
WATCHED_ACCOUNTS = {
    # 'blockbrothers': {            # account name (without the `@`)
    #     'weight': 100.0,          # vote percentage                           [defaults to 100%]
    #     'delay': 5 * MINUTE,      # minimum delay before voting               [defaults to 30min]
    #     'max_per_day': 2,         # maximum votes cast per day (=24h period)  [defaults to 1]
    # },
}
```

## 4. Check the logs
```bash
docker logs -f votebot
```
Votebot runs every 5 minutes, so it might take a few minutes before you see anything here.
There might be some errors if the votebot ran while you were still configuring it, but if properly setup it should look something like this:
```
2018-01-27 16:00:02 INFO     ### Running Votebot ###
2018-01-27 16:00:05 INFO     Voted on post "running-training-5-increasing-stamina" by @bennierex at 100.0%
2018-01-27 16:05:01 INFO     ### Running Votebot ###
...
```
Press `ctrl+c` to exit.

---

## Manual install
```bash
$ cd
$ git clone https://github.com/blockbrothers/votebot.git
$ cd votebot
$ docker build -t votebot:latest .
```

Then configure votebot (as detailed in Step 3):
```bash
$ mkdir ./config
$ cp ./settings.example.py ./config/settings.py
$ nano ./config/settings.py
```

Run the container:
```bash
$ docker run -v $(pwd)/config:/usr/src/votebot/config -d --name votebot -t votebot:latest
```

Setup the wallet (as detailed in Step 2):
```bash
$ docker exec -ti votebot steempy addkey
```

---

<div style="text-align: center;">
<p>If you support us please vote <a href="https://steemit.com/~witnesses">here</a> for <a href="/@blockbrothers">@blockbrothers</a><br>
<sup>Be sure to check that it says blockbrothers below the manual voting field.<br>
Only press 'VOTE’, the green round button will cancel your vote.</sup></p>
<p><a href="https://steemit.com/~witnesses"><img src="https://steemitimages.com/0x0/https://steemitimages.com/DQmVNgTBipBJkMFFQWxC5dtLDQgBHL3vxbzZZRrigcW9z1v/witnesvoting_crop.gif"></a><br>
<sup>Or you can choose to set blockbrothers as your proxy just below the manual vote</sup></p>
<p>
<a href="https://v2.steemconnect.com/sign/account-witness-vote?witness=blockbrothers&approve=1">Vote for @blockbrothers via SteemConnect</a><br>
<a href="https://v2.steemconnect.com/sign/account-witness-proxy?proxy=blockbrothers&approve=1">Set blockbrothers as your proxy via SteemConnect</a>
</p>
<hr>
<p><a href="https://steemit.com/@blockbrothers/"><img src="https://steemitimages.com/DQmdWG7QanG3ZEgJQ4SiLkyQ5BKtxGU7jrrnwDTqsz3r177/Logo_Side-by_side_1000.png"></a><br>
<sub>Makers of Steemify. The dedicated notification app for anything happening on the Steem blockchain<br>
Get it Here:
</sub></p>
<p><a href="https://itunes.apple.com/app/steemify/id1290154477" rel="noopener"><img src="https://steemitimages.com/0x0/https://steemitimages.com/DQmWPdFqXkrRZZ9xFnVjkfoNmYEXQRXd6FesJ1kAPFjkfmc/appstore.png"></a></p>
<p>Get in touch:<br>
<sup>
<a href="https://blockbrothers.io" rel="noopener">https://blockbrothers.io</a><br>
<a href="mailto:steemify@blockbrothers.io" rel="noopener">steemify@blockbrothers.io</a> | <a href="mailto:witness@blockbrothers.io" rel="noopener">witness@blockbrothers.io</a><br>
Telegram: <a href="https://t.me/blockbrothers" rel="noopener">https://t.me/blockbrothers</a></sup></p>
</div>
