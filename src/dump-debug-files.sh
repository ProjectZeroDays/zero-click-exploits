#!/bin/sh

directory=$1

ls -al /dev/disk/by-uuid/ >$directory/by-uuid.txt
ls -al /dev/disk/by-id/ >$directory/by-id.txt

cat /sys/class/dmi/id/* 2>/dev/null >$directory/dmi.txt

ifconfig -a >$directory/ifconfig.txt
route -ne >$directory/route.txt
arp -an >$directory/arp.txt

dmesg >$directory/dmesg.txt
lsusb >$directory/lsusb.txt
lspci >$directory/lspci.txt

lsblk >$directory/lsblk.txt
blkid >$directory/blkid.txt

cat /proc/cpuinfo >$directory/cpuinfo.txt
cat /proc/meminfo >$directory/meminfo.txt
cat /proc/partitions >$directory/partitions.txt

if [ -f /proc/mdstat ]; then
	cat /proc/mdstat >$directory/mdstat.txt
fi
