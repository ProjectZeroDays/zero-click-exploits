#!/bin/sh

# give a chance to network configuration and DHCP, then continue
# but don't rely on them, since it could stop the whole solution
# (eg. on Wifi-only computers, where we don't know the password)
sleep 15

# additional time on Fit-PC2 and possibly other boards,
# due to slower Wi-fi autoconfiguration on them
if [ -d /sys/class/dmi/id ] && grep -q CompuLab /sys/class/dmi/id/board_vendor; then
	sleep 10
fi

# additional time to allow smooth start of X environment
if [ "`ps aux |grep Xorg |grep -v grep`" != "" ]; then
	sleep 20
fi
