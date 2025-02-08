#!/bin/sh

encryption_mode=$1
keys_directory=$2
drive_serial=$3
key=$4


# Assign encryption key to given drive serial number, for later reuse.
# Avoid duplicates.

if [ "$keys_directory" != "" ] && [ -d $keys_directory ] && [ "$drive_serial" != "" ]; then
	file=$keys_directory/$drive_serial.$encryption_mode

	if ! grep -qFx $key $file 2>/dev/null; then
		echo $key >>$file
	fi
fi
