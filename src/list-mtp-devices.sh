#!/bin/sh

jmtpfs -l 2>/dev/null |grep -v ^Available |grep -v ^Device |sort |uniq |while read line; do
	BUS=`echo "$line" |cut -d, -f1 |tr -d '[:space:]'`
	DEV=`echo "$line" |cut -d, -f2 |tr -d '[:space:]'`

	vendor=`echo "$line" |cut -d, -f6 |tr -d '[:space:]'`
	model=`echo "$line" |cut -d, -f5 |cut -d'(' -f1 |sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]$//' -e 's/ /_/g'`

	echo "${vendor}_${model}_MTP:$BUS,$DEV"
done
