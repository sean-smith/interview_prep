#include <stdio.h>
#include <stdlib.h>


/*
Join is when you have a key in both tables:

users
user_hobbies


select users.name, user_hobies.hobby from users, user_hobbies where users.id = user_hobbies.user_id and hobby like '%soccer%';
*/

// Determine if a str2 is a subset of str1 eg. 'bat' is a substring of 'abate'
int substring(char *str1, char *str2) {
  if (str2[0] == '\0') {
    return 1;
  }
  if (str1[0] == '\0') {
    return 0;
  }
  if (str1[0] == str2[0]) {
    return substring(++str1, ++str2);
  }
  else {
    return substring(++str1, str2);
  }
}


int main(int argc, char **argv) {
  if (argc != 3) {
    printf("Please enter two arguments:\nsubstring [string1] [string2]\n");
    exit(0);
  }
  char *str1 = argv[1];
  char *str2 = argv[2];
  printf("substring(%s, %s) = %d\n", str1, str2, substring(str1, str2));
  return 0;
}