#!/usr/bin/env bash
length=${#1}
sum=0
for (( i = 0; i < $length; ++i )); do
    square=$(( ${1:$i:1} ** length ))
    sum=$(( sum+square ))
done

if [[ $sum == $1 ]]; then
    echo true
else
    echo false
fi