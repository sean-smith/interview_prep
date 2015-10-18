#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char *reverse(char *str1) {
	int len = strlen(str1);
	int j = len - 1;
	for (int i = 0; i < len && j > i; i++, j--) {
		char tmp = str1[i];
		str1[i] = str1[j];
		str1[j] = tmp;
	}
	return str1;
}


int main(int argc, char **argv) {
	printf("%s\n",reverse(argv[1]));
	return 0;
}


