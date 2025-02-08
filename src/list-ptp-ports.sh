#!/bin/sh

gphoto2 --auto-detect |grep usb: |cut -d: -f2 |sed -e "s/^/usb:/"
