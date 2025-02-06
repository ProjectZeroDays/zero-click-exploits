#!/bin/bash

target_root_directory=$1
target_directory=$2
keys_directory=$3
drive_serial=$4
current_partition=$5
uuid=$6


slices=`/opt/drivebadger/internal/generic/apple/get-apfs-filesystems.sh /dev/$current_partition`
for slice in $slices; do
	slid="${slice%:*}"
	slname="${slice##*:}"

	mountpoint=/media/$current_partition/$slid/mnt
	subtarget=$target_directory/$drive_serial/${current_partition}_apfs_${slid}_${slname}
	mkdir -p $mountpoint $subtarget

	if /opt/drivebadger/internal/generic/apple/mount-apfs-filesystem.sh $keys_directory "$drive_serial" /dev/$current_partition $slid $mountpoint $subtarget >>$subtarget/rsync.log 2>>$subtarget/rsync.err; then
		/opt/drivebadger/internal/generic/process-hooks.sh $mountpoint $target_root_directory

		logger "copying UUID=$uuid (partition $current_partition filesystem APFS slice $slid ($slname), mounted as $mountpoint, target directory $subtarget)"
		/opt/drivebadger/internal/generic/rsync-partition.sh $mountpoint $subtarget >>$subtarget/rsync.log 2>>$subtarget/rsync.err
		umount $mountpoint
		logger "copied UUID=$uuid"
	fi
done
