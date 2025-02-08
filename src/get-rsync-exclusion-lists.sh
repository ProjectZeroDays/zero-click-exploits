#!/bin/sh

for list in `ls /opt/drivebadger/config/*/exclude.list`; do
	echo -n " --exclude-from=$list"
done

for script in `ls /opt/drivebadger/hooks/*/exclude.sh 2>/dev/null`; do
	$script $1
done
