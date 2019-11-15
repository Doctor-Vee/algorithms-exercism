#!/usr/bin/env bash
if [[ $# == 2 ]]; then
    length1=${#1}
    length2=${#2}
    if ! [[ $length1 == $length2 ]] ; then
        echo "left and right strands must be of equal length"
        exit 1
    fi

    for (( i = 0; i < $length1; ++i )); do
        if [[ ${1:$i:1} != ${2:$i:1} ]]; then
        count=$(( count+1 ))
        fi
    done
    [[ -z $count ]] && echo "0" || echo $count

else
    echo "Usage: hamming.sh <string1> <string2>"
    exit 1
fi