#include <stdlib.h>
#include <stdio.h>


/*
 * Given a array with zeroes in it,
 * Transform that array to an array with
 * zeroes at the end.
 *
 * Example:
 * [ 1, 2, 0, 4, 5, 6, 0 ]
 * 	Becomes:
 * [ 1, 2, 4, 5, 6, 0, 0 ]
 */

void zeroesatend(int *a, int size)
{
	int p1 = 0;
	int p2 = 0;

	while (p1 < size) {
		if (a[p1] == 0) {
			p1++;
		} else {
			a[p2] = a[p1];
			p2++;
			p1++;
		}
	}
	while (p2 < size) {
		a[p2] = 0;
		p2++;
	}
}

void printarray (int *a, int size) {
	printf("[ ");
	for (int i = 0; i < size; i++) {
		printf("%d, ", a[i]);
	}
	printf("]\n");
}


int main()
{
	int a[7] = {1, 2 , 0, 4, 5, 6, 0};
	printarray(a, sizeof a / sizeof *a);
	zeroesatend(a, sizeof a / sizeof *a);
	printarray(a, sizeof a / sizeof *a);
	return 0;
}