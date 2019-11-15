#!/usr/bin/env bash

if [[ $(( $1%3 )) == 0  ]]; then
  result+="Pling"
fi
if [[ $(( $1%5 )) == 0  ]]; then
  result+="Plang"
fi
if [[ $(( $1%7 )) == 0  ]]; then
  result+="Plong"
fi
if [[ $result == ""  ]]; then
  result+=$1
fi
echo $result



# # Below is someone else's solution which I found in the community after submitting mine
# (( $1%3 == 0 )) && sound="Pling"
# (( $1%5 == 0 )) && sound+="Plang"
# (( $1%7 == 0 )) && sound+="Plong"

# [[ -z "$sound" ]] && echo "$1" || echo "$sound"