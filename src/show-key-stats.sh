#!/bin/sh

keys_directory=`/opt/drivebadger/internal/mobile/get-keys-directory.sh`

/opt/drivebadger/internal/generic/keys/show-key-stats.sh $keys_directory
