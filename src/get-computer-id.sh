#!/bin/sh

comp_name=`cat /sys/class/dmi/id/product_name |sed -e 's/[ \t]*$//' -e 's/ /_/g'`
local_ip=`ifconfig -a |grep -v 127.0.0.1 |grep 'inet ' |awk '{ print $2 }' |head -n 1`

logger "computer name $comp_name, primary IP $local_ip"

echo ${local_ip}_${comp_name}
