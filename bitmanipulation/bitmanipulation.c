#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Write a function that maps:
// f(1) -> 2
// f(2) -> 1

int f0(int x) 
{
	return x == 2 ? 1 : 2; 
}

int f1(int x)
{
	if (x == 2) {
		return 1;
	}else {
		return 2;
	} 
}

// Now no conditionals

// 10 ^ 11 = 01
// 01 ^ 11 = 10

int f2(int x)
{
	return x ^ 3;
}

// 10 >> 1 = 01
// 01 >> 1 = 00
// 10 << 1 = 100 & 11 = 00
// 01 << 1 = 10

int f3(int x)
{
	return ((x << 1) & 3) ^ (x >> 1);
}


// Work in progress
// Same as xor 3 and negating then masking

int f4(int x)
{
	return (3 - x);
}

// Same as left/right shift

int f5(int x)
{
	return ((x*2) & 3) ^ (x / 2);
}

int f6(int x)
{
	return (~x & 3);
}

int f7(int x)
{
	switch (x) {
		case 1:
			return 2;
		default:
			return 1;
	}
}

int f8(int x)
{
	return (int)pow(2, 2-x);
}

int f9(int x)
{
	return (x % 2) + 1;
}


int main(int argc, char** argv) {
	printf("f0(1) = %d, f0(2) = %d\n", f0(1), f0(2));
	printf("f1(1) = %d, f1(2) = %d\n", f1(1), f1(2));
	printf("f2(1) = %d, f2(2) = %d\n", f2(1), f2(2));
	printf("f3(1) = %d, f3(2) = %d\n", f3(1), f3(2));
	printf("f4(1) = %d, f4(2) = %d\n", f4(1), f4(2));
	printf("f5(1) = %d, f5(2) = %d\n", f5(1), f5(2));
	printf("f6(1) = %d, f6(2) = %d\n", f6(1), f6(2));
	printf("f7(1) = %d, f7(2) = %d\n", f7(1), f7(2));
	printf("f8(1) = %d, f8(2) = %d\n", f8(1), f8(2));
	printf("f9(1) = %d, f9(2) = %d\n", f9(1), f9(2));

	return 1;
}
