#!/bin/sh

if [ "$1" = "" ]; then
	echo "usage: $0 [keys-directory]"
	exit 0
elif [ ! -d $1 ]; then
	echo "error: invalid keys directory $1"
	exit 1
fi

keys_directory=$1
tmpfile=`mktemp -p /run`

echo "encryption mode | keys assigned to drives | repo keys unassigned | common | total repo keys | unique repo keys"
echo "--------------------------------------------------------------------------------------------------------------"

for encryption_mode in apfs bitlocker luks veracrypt; do

	keys_assigned=`cat $keys_directory/*.$encryption_mode 2>/dev/null |wc -l`
	cat $keys_directory/*.$encryption_mode 2>/dev/null >$tmpfile

	keys_unassigned=`cat /opt/drivebadger/config/*/$encryption_mode.keys 2>/dev/null |grep -v "^#" |grep -v ^$ |grep -vxFf $tmpfile |wc -l`
	keys_common=`cat /opt/drivebadger/config/*/$encryption_mode.keys 2>/dev/null |grep -v "^#" |grep -v ^$ |grep -xFf $tmpfile |wc -l`
	keys_total_repos=`cat /opt/drivebadger/config/*/$encryption_mode.keys 2>/dev/null |grep -v "^#" |grep -v ^$ |wc -l`
	keys_total_unique=`cat /opt/drivebadger/config/*/$encryption_mode.keys 2>/dev/null |grep -v "^#" |grep -v ^$ |sort |uniq |wc -l`

	printf "%-15s | %-23d | %-20d | %-6d | %-15d | %d \n" $encryption_mode $keys_assigned $keys_unassigned $keys_common $keys_total_repos $keys_total_unique |sed 's/ 0 /   /g'
done

rm -f $tmpfile
