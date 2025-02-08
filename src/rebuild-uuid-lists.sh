#!/bin/sh

TYPES="target ignore"

for TYPE in $TYPES; do
	FILE=/var/cache/drivebadger/$TYPE.uuid.generated
	echo "# generated at `date`" >$FILE.new
	cat /opt/drivebadger/config/*/$TYPE.uuid |grep -v ^$ |grep -v "^#" >>$FILE.new
	mv -f $FILE.new $FILE
done
