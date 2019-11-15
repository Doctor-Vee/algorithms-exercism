#!/usr/bin/env bash
if [[ $# == 1 ]]; then
    re='^[0-9]+$'
    if ! [[ $1 =~ $re ]] ; then
    #copied the above line from stackoverflow (https://stackoverflow.com/questions/806906/how-do-i-test-if-a-variable-is-a-number-in-bash)
        echo "Usage: leap.sh <year>"
        exit 1
    fi

    if [[ $(( $1 % 4 )) == 0 && $(( $1 % 100 )) != 0 || $(( $1 % 400 )) == 0 ]]; then
        echo "true"
    else
        echo "false"
    fi
else
    echo "Usage: leap.sh <year>"
    exit 1
fi