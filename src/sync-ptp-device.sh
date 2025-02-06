#!/bin/sh

PORT=$1
LOG=$2
DEBUG=$3

if [ "$DEBUG" != "" ]; then
	gphoto2 --debug --debug-logfile=$DEBUG --get-all-files --skip-existing --port $PORT >>$LOG
else
	gphoto2 --get-all-files --skip-existing --port $PORT >>$LOG
fi
