#!/bin/sh

keys_directory=$1
drive_serial=$2
device=$3
slice=$4
mountpoint=$5
subtarget=$6

if fsapfsmount -f $slice $device $mountpoint; then
	exit 0
fi

for recovery_key in `/opt/drivebadger/internal/generic/keys/get-drive-encryption-keys.sh apfs $keys_directory $drive_serial`; do
	if fsapfsmount -f $slice -p$recovery_key $device $mountpoint; then
		echo $recovery_key >$subtarget/apfs.key
		/opt/drivebadger/internal/generic/keys/save-drive-encryption-key.sh apfs $keys_directory $drive_serial $recovery_key
		exit 0
	fi
done

exit 1
