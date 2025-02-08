#!/bin/sh

PORT=$1
FILE=$2

gphoto2 --summary --port $PORT 2>/dev/null >$FILE

# data transfer from other PTP device in progress
if grep -q '^For debugging messages' $FILE; then
	rm -f $FILE
	exit 0
fi

if grep -q ^Manufacturer: $FILE; then
	vendor=`grep ^Manufacturer: $FILE |cut -d: -f2 |tr -d '[:space:]'`
	model=`grep ^Model: $FILE |cut -d: -f2 |tr -d '[:space:]'`
	serial=`grep 'Serial Number:' $FILE |cut -d: -f2 |tr -d '[:space:]'`
	echo "${vendor}_${model}_${serial}_PTP" |tr ',' '-' |tr -d '.()'
else
	gphoto2 --abilities --port $PORT 2>/dev/null |grep -v MTP |grep ^Abilities |cut -d: -f2 |sed -e 's/^[[:space:]]*//' -e 's/ /_/g'
fi
