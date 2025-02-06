#!/bin/sh

encryption_mode=$1
keys_directory=$2
drive_serial=$3


# 1. Try to find key(s) assigned to given drive serial number:
#    - preconfigured manually
#    - found during previous Drive Badger runs
# 2. Print generic keys, preconfigured using configuration repositories

file=""
if [ "$keys_directory" != "" ] && [ "$drive_serial" != "" ]; then
	file=$keys_directory/$drive_serial.$encryption_mode
fi

if [ "$file" != "" ] && [ -s $file ]; then
	cat $file
	cat /opt/drivebadger/config/*/$encryption_mode.keys 2>/dev/null |grep -v "^#" |grep -v ^$ |grep -vxFf $file
else
	cat /opt/drivebadger/config/*/$encryption_mode.keys 2>/dev/null |grep -v "^#" |grep -v ^$
fi
