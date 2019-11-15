#include "raindrops.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *convert(char result[], int drops) {
    if (drops%3==0 && drops%5==0 && drops%7==0){
        return "PlingPlangPlong";
    } else if (drops%3==0 && drops%5==0){
        return "PlingPlang";
    } else if (drops%3==0 && drops%7==0){
        return "PlingPlong";        
    } else if (drops%5==0 && drops%7==0){
        return "PlangPlong"; 
    } else if (drops%3==0){
        return "Pling";
    } else if (drops%5==0){
        return "Plang";
    } else if (drops%7==0){
        return "Plong";
    } else {
        return drops;
    }
}

int main(void){
    printf("%s\n", convert("Hello", 5));
}

// #include <stdio.h>
// int main()
// {
//     char s1[100], s2[100], i, j;
//     printf("Enter first string: ");
//     scanf("%s", s1);
//     printf("Enter second string: ");
//     scanf("%s", s2);
//     // calculate the length of string s1
//     // and store it in i
//     for (i = 0; s1[i] != '\0'; ++i)
//         ;
//     for (j = 0; s2[j] != '\0'; ++j, ++i)
//     {
//         s1[i] = s2[j];
//     }
//     s1[i] = '\0';
//     printf("After concatenation: %s\n", s1);
//     return 0;
// }