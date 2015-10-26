#include <stdio.h>
#include <stdlib.h>


/*
Join is when you have a key in both tables:

users
user_hobbies


select users.name, user_hobies.hobby from users, user_hobbies where users.id = user_hobbies.user_id and hobby like '%soccer%';
*/

// Determine if a string is a subset of another string eg. 'bat' is a substring of 'abate'
// To execute C, please define "int main()"

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


/*
Your previous Python content is preserved below:


# 
# Your previous Plain Text content is preserved below:
# 
# Input will be an list  with duplicates and your code should remove the duplicates.
# 

# Take a list and hash values into a dictionary
# for each subsequent value look up the hash to determine if it's duplicated


def removeDups(list):
    duplicates = {}
    i = 0
    length_of_list = len(list)
    while(i < length_of_list):
        value = list[i]
        if value in duplicates:
            list.remove(value)
            length_of_list -= 1
        else:
            duplicates[value] = 1
            i+= 1
            
            
    print list
    
removeDups([1,2,2, 3, 4, 3, 4])




*/

