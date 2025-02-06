#!/bin/sh

# Discover subdirectory inside target drive (all copied data is stored inside
# hidden subdirectory to prevent accidental showing such data to 3rd party in
# case of forced inspection etc. - it's definitely not enough to call it
# "secure", however it's often enough in real life).

BASE="/media/target"
FALLBACK="/media/fallback"

if [ -d $BASE/.support/.files ]; then
	SUBDIR=$BASE/.support/.files
elif [ -d $BASE/.files/.data ]; then
	SUBDIR=$BASE/.files/.data
elif [ -d $BASE/files/data ]; then
	SUBDIR=$BASE/files/data
else
	SUBDIR=$FALLBACK
fi

TARGET="$SUBDIR/`date +%Y%m%d`"
mkdir -p $TARGET
echo $TARGET
