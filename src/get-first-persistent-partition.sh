#!/bin/sh

# FIXME: this can work improperly, if:
#  - user connects 2 Kali Linux Live USB drives
#  - the first one is NVMe
#  - the second is not NVMe
#  - Kali Linux will be booted from the second one
#  - first persistent partition after boot will be mounted from the first one
#
# sample output from get-persistent-partitions.sh:
#
#    /dev/mapper/sdb3
#    /dev/mapper/sdc3
#
# and medium should be eg. "sdb" (this allows choosing the proper partition)
# or empty (first persistent partition is most usually the correct one)
#
medium=`mount |grep live/medium |grep iso9660 |grep ^/dev/sd |cut -d' ' -f1 |sed -e 's/\/dev\///g' -e 's/[0-9]//g'`


if [ "$medium" != "" ]; then
	/opt/drivebadger/internal/kali/get-persistent-partitions.sh |grep "$medium"
else
	/opt/drivebadger/internal/kali/get-persistent-partitions.sh |head -n 1
fi
