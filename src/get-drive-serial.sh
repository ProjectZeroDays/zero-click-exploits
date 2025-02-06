#!/bin/bash

drive=$1
directory=$2

if [ ! -f $directory/$drive.txt ]; then
	if [[ $drive =~ ^mmc ]]; then
		udevadm info -a /dev/$drive >$directory/$drive.txt
	elif [[ $drive =~ ^nvme ]]; then
		nvme id-ctrl /dev/$drive >$directory/$drive.txt
	else
		hdparm -I /dev/$drive >$directory/$drive.txt
	fi
fi

if [[ $drive =~ ^mmc ]]; then
	grep 'ATTRS{serial}' $directory/$drive.txt |tr -d ' \t\"' |tr '=' ' ' |awk '{ print $2 }'
elif [[ $drive =~ ^nvme ]]; then
	cat $directory/$drive.txt |tr -d ' \t' |grep ^sn: |cut -d':' -f2
elif grep -q "Serial Number" $directory/$drive.txt; then
	cat $directory/$drive.txt |tr -d ' \t' |grep ^SerialNumber: |cut -d':' -f2
else
	ls -l /dev/disk/by-id/* |grep /$drive$ |grep -v wwn- |cut -d'/' -f5 |cut -d'-' -f2- |sed -e "s/ -> ..//g" -e "s/-0:0//g"
fi
