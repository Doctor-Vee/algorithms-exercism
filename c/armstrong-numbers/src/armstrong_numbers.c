#include "armstrong_numbers.h"

#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isArmstrongNumber(int x)
{
    int y = x;
    int count = 0;
    int sum = 0;
    int digit;
    while (y)
    {
        y = y/10;
        count++;
    }
    y = x;
    for (int i = 0; i<count; i++){
        digit = y%10;
        sum += pow(digit,count);
        y = y/10;
    }

    return (sum == x) ? true : false;
}
