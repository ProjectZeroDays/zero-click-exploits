#!/bin/sh

perdev=`/opt/drivebadger/internal/kali/get-first-persistent-partition.sh`

if [ "$perdev" != "" ]; then
	target_partition=`basename $perdev`
	target_root_directory=`/opt/drivebadger/internal/kali/get-target-directory.sh $target_partition`
	target_base=`dirname $target_root_directory`
	tsp |sed -r -e "s#/opt/drivebadger/hooks/hook-virtual/handle-image.sh ##g" -e "s#/media/(.*)/mnt/#\1 #g" -e "s#/media/(.*)/mnt##g" -e "s#$target_base/##g"
else
	tsp |sed -r -e "s#/opt/drivebadger/hooks/hook-virtual/handle-image.sh ##g" -e "s#/media/(.*)/mnt/#\1 #g" -e "s#/media/(.*)/mnt##g"
fi
