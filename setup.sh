#!/usr/bin/env bash

echo "INSTALLING Votebot"

unset CDPATH
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

sudo apt-get update && sudo apt-get -y install make autoconf automake libtool m4 libssl-dev libreadline-dev libsqlite3-dev zlib1g-dev gzip bzip2 bison g++ wget curl git

if ! [ -x "$(command -v pyenv)" ]; then
    echo "Installing pyenv"
    # Install pyenv
    curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

    source ~/.bashrc
fi

echo "=> Installing Python"
# Install Python 3.6
pyenv install 3.6.4
# Create virtualenv
pyenv virtualenv 3.6.4 votebot

echo "=> Setting up virtual environment"
# Activate virtualenv
cd && cd $DIR

# Setup virtual environment
pip install --upgrade pip
pip install --upgrade setuptools
pip install -r ./requirements.txt

sed -i 's/toml==0\.9\.3\.1/toml==0\.9\.3/' $(find $PYENV_VIRTUAL_ENV/lib/python3.6/site-packages/steem-* -name requires.txt)
pip install toml==0.9.3

steempy set nodes https://api.steemit.com,https://steemd.minnowsupportproject.org,https://gtg.steem.house:8090,https://steemd.privex.io,https://steemd.pevo.science,https://rpc.steemliberator.com

echo "=> Enter your POSTING key and (new) wallet passphrase. Press Enter when done."
steempy addkey

CONFIGFILE="$DIR/config.py"
if ! [ -e $CONFIGFILE ]; then
    mv "$DIR/config.example.py" $CONFIGFILE
fi
chmod 0600 $CONFIGFILE

# Deactivate virtualenv
cd

chmod +x "$DIR/run.sh"

echo "#####################################################"
echo ""
echo "Be sure to edit ${CONFIGFILE} before running Votebot."
echo "Add the following line to your crontab:"
echo "*/5 * * * * $DIR/run.sh > /dev/null 2>&1"
echo ""
echo "#####################################################"
echo ""
echo "FINISHED INSTALLING Votebot"
