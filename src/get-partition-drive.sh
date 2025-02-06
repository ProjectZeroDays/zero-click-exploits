#!/bin/bash

partition=$1

if [[ $partition =~ ^dm ]] || [[ $partition =~ ^md ]]; then
	echo $partition  # is it enough to properly support various RAID types?
elif [[ $partition =~ ^mmc ]] || [[ $partition =~ ^nvme ]]; then
	echo $partition |cut -dp -f1
else
	echo $partition |sed 's/[0-9]//g'  # sdx or sdxy
fi
