#!/bin/sh

src=$1
target=$2
lists=`/opt/drivebadger/internal/generic/get-rsync-exclusion-lists.sh $src`

echo "### BEGIN `date +'%Y-%m-%d %H:%M:%S'` ###"

rsync -av $lists $src $target

echo "### END `date +'%Y-%m-%d %H:%M:%S'` ###"
