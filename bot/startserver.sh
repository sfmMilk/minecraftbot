#!/bin/bash
PARENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd $PARENT_DIR/bot # Changes directory to bot. That way I can find config bash lol
source ./config/config.sh
cd ./.. # Go up a level outside of bot, this is where your minecraftservers SHOULD be.

if [ -d "./$SERVER_NAME" ]; then
    cd ./$SERVER_NAME
    screen -dmS bash -c './start.sh' # ASSUMES start.sh IS REAL!! DANGEROUS!!
else
    echo "$SERVER_NAME does not exist!"
fi

# To the Caleb of whenever he decides to read this. Please make/learn functions in bash. This is ugly. Also it's unfinished.


