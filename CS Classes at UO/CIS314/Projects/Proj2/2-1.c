#include <stdio.h>
#define UI unsigned int

UI mask(int n) {
	UI nMask = 0x1  << n; // mask and shift
	UI nSubRes = nMask - 1; // subtract 1 from shifted mask


	return nSubRes; // results
	
}

int main() {
	printf("mask(1): 0x%X\n", mask(1));
	printf("mask(2): 0x%X\n", mask(2));
	printf("mask(3): 0x%X\n", mask(3));
	printf("mask(5): 0x%X\n", mask(5));
	printf("mask(8): 0x%X\n", mask(8));
	printf("mask(16): 0x%X\n", mask(16));
	printf("mask(31): 0x%X\n", mask(31));
}
