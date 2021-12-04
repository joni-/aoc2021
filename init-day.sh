#!/bin/bash

day=$1

if [ -z $day ]
then
    echo "Usage: $0 <day>"
    exit 1
fi

./fetch.sh $day
./copy-files.sh $day