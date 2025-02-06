#!/bin/sh

# The below logic is responsible for selecting, which script (only one!)
# will be executed against the drive mounted in read/write mode.

fs=$1
drive_serial=$2
uuid=$3


#
# Match exact partition using its UUID.
#
# Downside: Bitlocker and VeraCrypt partitions can't be handled this way.
#
if [ "$uuid" != "" ] && [ -x /opt/drivebadger/injectors/uuid-$uuid/injector.sh ]; then
	echo /opt/drivebadger/injectors/uuid-$uuid/injector.sh

#
# Match the drive and partition type, but not the exact partition - so this
# injector will be run against all partitions of given type (eg. NTFS).
#
# You are responsible for implementing checks eg. for specific directory,
# or any other condition(s) unique to the exact filesystem, that you're
# trying to match.
#
elif [ "$drive_serial" != "" ] && [ -x /opt/drivebadger/injectors/$fs-$drive_serial/injector.sh ]; then
	echo /opt/drivebadger/injectors/$fs-$drive_serial/injector.sh

#
# Run this injector for all partitions of given type (eg. NTFS),
# that were not matched by any specific injector.
#
elif [ -x /opt/drivebadger/injectors/$fs/injector.sh ]; then
	echo /opt/drivebadger/injectors/$fs/injector.sh
fi
