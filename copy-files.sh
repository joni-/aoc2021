#!/bin/bash

day=$1

if [ -z $day ]
then
    echo "Usage: $0 <day>"
    exit 1
fi

cat day.template | sed -E "s/XXX/$day/g" > day$(printf "%02d" $day).py
cat tests/test.template | sed -E s/XXX/day$(printf "%02d" $day)/g > tests/test_day$(printf "%02d" $day).py
