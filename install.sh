#!/bin/bash

DIR="/usr/local/bin";
NAME="katoolin3";

cp ./katoolin3.py "$DIR/$NAME" || exit 1;
chmod 555 "$DIR/$NAME" || exit 1;
apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6 || exit 1;
apt-get -qq -y -m install python3-apt || exit 1;

echo "Successfully installed. Run it with '$NAME'.";
