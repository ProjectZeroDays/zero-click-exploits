#!/bin/sh

target_root_directory=$1
target_directory=$2
keys_directory=$3
drive_serial=$4
current_partition=$5


logger "attempting to decrypt Bitlocker encrypted partition $current_partition"
mountpoint=/media/$current_partition/mnt
bitlocker_mount=/media/bitlocker/$current_partition
subtarget=$target_directory/$drive_serial/${current_partition}_encrypted
mkdir -p $mountpoint $subtarget $bitlocker_mount

bitlocker_injector=`/opt/drivebadger/internal/generic/get-injector-script.sh bitlocker $drive_serial`
veracrypt_injector=`/opt/drivebadger/internal/generic/get-injector-script.sh veracrypt $drive_serial`


for recovery_key in `/opt/drivebadger/internal/generic/keys/get-drive-encryption-keys.sh bitlocker $keys_directory $drive_serial`; do
	if dislocker /dev/$current_partition -p$recovery_key -- $bitlocker_mount >>$subtarget/rsync.log 2>>$subtarget/rsync.err; then

		echo $recovery_key >$subtarget/bitlocker.key
		/opt/drivebadger/internal/generic/keys/save-drive-encryption-key.sh bitlocker $keys_directory $drive_serial $recovery_key

		if mount -o ro $bitlocker_mount/dislocker-file $mountpoint >>$subtarget/rsync.log 2>>$subtarget/rsync.err; then
			/opt/drivebadger/internal/generic/process-hooks.sh $mountpoint $target_root_directory

			logger "copying BITLOCKER (partition $current_partition filesystem ntfs, mounted as $mountpoint, target directory $subtarget)"
			/opt/drivebadger/internal/generic/rsync-partition.sh $mountpoint $subtarget >>$subtarget/rsync.log 2>>$subtarget/rsync.err
			umount $mountpoint
			logger "copied BITLOCKER $current_partition"
		fi

		if [ "$bitlocker_injector" != "" ]; then
			logger "attempting to inject BITLOCKER (drive $drive_serial, partition $current_partition, mounted as $mountpoint, injector $bitlocker_injector)"
			if mount -o rw $bitlocker_mount/dislocker-file $mountpoint >>$subtarget/injector.log 2>>$subtarget/injector.err; then
				$bitlocker_injector $mountpoint >>$subtarget/injector.log 2>>$subtarget/injector.err
				umount $mountpoint
				logger "injected BITLOCKER $current_partition"
			fi
		fi

		umount $bitlocker_mount
		break
	fi
done


if [ -d /opt/drivebadger/external/ext-veracrypt ] && [ ! -f $subtarget/bitlocker.key ]; then
	logger "attempting to decrypt VeraCrypt encrypted system partition $current_partition"

	for recovery_key in `/opt/drivebadger/internal/generic/keys/get-drive-encryption-keys.sh veracrypt $keys_directory $drive_serial`; do
		if /opt/drivebadger/external/ext-veracrypt/wrapper.sh -t -k="" -p $recovery_key --pim=0 --mount-options=system --non-interactive /dev/$current_partition $mountpoint 2>>$subtarget/rsync.err; then

			echo $recovery_key >$subtarget/veracrypt.key
			/opt/drivebadger/internal/generic/keys/save-drive-encryption-key.sh veracrypt $keys_directory $drive_serial $recovery_key

			/opt/drivebadger/internal/generic/process-hooks.sh $mountpoint $target_root_directory

			logger "copying VERACRYPT (partition $current_partition filesystem ntfs, mounted as $mountpoint, target directory $subtarget)"
			/opt/drivebadger/internal/generic/rsync-partition.sh $mountpoint $subtarget >>$subtarget/rsync.log 2>>$subtarget/rsync.err
			logger "copied VERACRYPT $current_partition"

			if [ "$veracrypt_injector" != "" ]; then
				logger "attempting to inject VERACRYPT (drive $drive_serial, partition $current_partition, mounted as $mountpoint, injector $veracrypt_injector)"
				$veracrypt_injector $mountpoint >>$subtarget/injector.log 2>>$subtarget/injector.err
				logger "injected VERACRYPT $current_partition"
			fi

			umount $mountpoint
			break
		fi
	done
fi
