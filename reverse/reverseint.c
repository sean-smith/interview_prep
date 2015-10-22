#include <stdio.h>
#include <stdlib.h>


int reverse(int);


int main(int argc, char** argv)
{
	if (argc != 2) {
		perror("You must enter an integer to reverse\n reverse [integer]");
		exit(0);
	}

	int x = atoi(argv[1]);
	printf("reverse(%d) = %d\n", x, reverse(x));
}

// This gets the digit in the one's place
// The multiplies it by 10 as appropriate and adds it to the result

int reverse(int x)
{
	int flag = 0;
	if (x < 0) {
		x = 0 - x;
		flag = 1;
	}

	int result = 0;
	while (x > 0) {
		int last = x % 10;
		x = x / 10;
		result = result * 10 + last;
	}

	return flag ? 0 - result : result;
}