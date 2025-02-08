#!/bin/sh

device=$1

fsapfsinfo $device \
	|grep -A2 Volume \
	|grep -v Identifier \
	|sed -e 's/[\t ]//g' -e 's/information://g' -e 's/Volume://g' -e 's/Name://g' -e 's/[^a-zA-Z0-9]//g' \
	|tr '\n' ':' \
	|sed -e 's/::/\n/g' -e 's/:$//g' \
	|egrep -v ':(Preboot|Recovery|VM)$'
