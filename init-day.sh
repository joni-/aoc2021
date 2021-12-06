#!/bin/bash

day=$1

if [ -z $day ]
then
    echo "Usage: $0 <day>"
    exit 1
fi

./copy-files.sh $day
./fetch.sh $day
