#include "pangram.h"
#include <stdio.h>
#include <ctype.h>
#include <string.h>

bool is_pangram(const char sentence[]){
  if (sentence == NULL){
    return false;
  }
  int length = strlen(sentence);
  char result[length+1]; //+1 for \0
  for(int i = 0; i < length; i++){
    result[i] = toupper(sentence[i]);
  }
  char a;
  int count = 0;
  for (int i = 65; i < 91; i++){
    a = i;
    for (int j = 0; j < length; j++){
      if (a == result[j]){
        count=1;
        break;
      }
    }
    if (count != 1) return false;
    count = 0;
  }

  return true;
}