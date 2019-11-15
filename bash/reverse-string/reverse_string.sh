#!/usr/bin/env bash

echo $1 | rev # The | means that it takes the value of string1 and pipes it to the rev (reverse) built in function

# chmod u+x reverse_string.sh

# string=$1
# length=$(( ${#string} - 1 )) 
# stringer=""

# while [ $length -gt -1 ]; do
#     stringer+=${string:$length:1}
#     ((length--))
# done

# echo $string | rev
# exit 0
