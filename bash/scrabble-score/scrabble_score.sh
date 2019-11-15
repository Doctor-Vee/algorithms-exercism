#!/usr/bin/env bash
score=0
for (( i = 0; i < ${#1}; ++i )); do
    case ${1:$i:1} in
        [aA]|[eE]|[iI]|[oO]|[uU]|[lL]|[nN]|[rR]|[sS]|[tT])
        ((score+=1))
        ;;
        [dD]|[gG])
        ((score+=2))
        ;;
        [bB]|[cC]|[mM]|[pP])
        ((score+=3))
        ;;
        [fF]|[hH]|[vV]|[wW]|[yY])
        ((score+=4))
        ;;
        [kK])
        ((score+=5))
        ;;
        [jJ]|[xX])
        ((score+=8))
        ;;
        [qQ]|[zZ])
        ((score+=10))
        ;;
    esac
done

echo $score