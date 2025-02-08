#!/bin/sh

partition=$1
directory=$2

if [ ! -f $directory/$partition.txt ]; then
	udevadm info --query=all --name=/dev/$partition >$directory/$partition.txt
fi

grep ID_FS_TYPE $directory/$partition.txt |cut -d'=' -f2
