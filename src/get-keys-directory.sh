#!/bin/sh

# In Drive Badger mode, keys_directory is created if not exists. This is ok, because
# Drive Badger is meant to be used mostly with encrypted storage - so keys are also
# encrypted.
#
# On the other hand, Mobile Badger can only use unencrypted storage, so administrator
# has to choose, if/where to create this directory - and create it manually.
#
# If keys_directory is not present (not created manually) on target drive, then the
# one from internal SD storage will be used.

BASE="/media/target"
FALLBACK="/etc/drivebadger/keys"

if [ -d $BASE/.support/.keys ]; then
	echo $BASE/.support/.keys
elif [ -d $BASE/.files/.keys ]; then
	echo $BASE/.files/.keys
elif [ -d $BASE/files/keys ]; then
	echo $BASE/files/keys
else
	echo $FALLBACK
fi
