#!/bin/bash

if [[ ! -f /usr/src/votebot/config/settings.py ]]; then
    echo "settings.py not found. Copying example settings file.";
    cp /usr/src/votebot/settings.example.py /usr/src/votebot/config/settings.py
fi

cron -f
