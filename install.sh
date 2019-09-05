#!/bin/bash

DIR="/usr/local/bin";
NAME="katoolin3";

cp ./katoolin3.py "$DIR/$NAME" || exit 1;
chmod +x "$DIR/$NAME" || exit 1;

echo "Successfully installed. Invoke by typing '$NAME'.";