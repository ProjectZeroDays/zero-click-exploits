#!/bin/sh

partitions=`mount |grep live/persistence |grep -v 'type overlay' |grep -v 'type iso9660' |grep rw |cut -d' ' -f1`

for part in $partitions; do
	if [ -f /run/live/persistence/`basename $part`/persistence.conf ]; then
		echo $part
	fi
done
