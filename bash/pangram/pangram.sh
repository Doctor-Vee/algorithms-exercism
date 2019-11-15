#!/usr/bin/env bash

sentence=${1^^}
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for (( i = 0; i < 26; ++i )); do
        if ! [[ $sentence == *${alpha:$i:1}* ]]; then
        echo false
        exit 0
        fi
    done
echo true