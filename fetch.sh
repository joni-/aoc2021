#!/bin/bash

day=$1

if [ -z $day ]
then
    echo "Usage: $0 <day>"
    exit 1
fi

source .cookie
filename=inputs/day$(printf "%02d" $day).in

year=2021
curl -sS --cookie session=$session --output $filename https://adventofcode.com/$year/day/$day/input
