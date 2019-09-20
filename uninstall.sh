#!/bin/bash

source "conf.sh";

rm -f "$DIR/$PROGRAM" || die "Uninstallation failed.";

echo "Successfully uninstalled.";
exit 0;