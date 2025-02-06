#!/bin/sh

device=$1

if [ "$device" != "" ]; then
	dm=`readlink $device`

	if [ "$dm" != "" ]; then  # eg. /dev/mapper/sdb3 -> /dev/dm-0 -> echo dm-0
		basename $dm
	else  # /dev/sdb3 -> echo sdb3
		basename $device
	fi
fi
