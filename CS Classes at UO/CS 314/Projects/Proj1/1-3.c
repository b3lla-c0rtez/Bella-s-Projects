#include <stdio.h>
#define UI unsigned int

int oddBit(UI x){
	UI aMask = 0b10101010101010101010101010101010; //32-bit mask of 1s and 0s, 1s represent odd numbers and 0s represent even numbers

	UI a = aMask & x; //using the mask and applying it to x
	UI b = !!a; //doing two nots of a (applying two logical nots; not a -> not not a)
	return b; //returning output of b
}

int main() {
	printf("oddBit(0x1): %X\n", oddBit(0x1));
	printf("oddBit(0x2): %X\n", oddBit(0x2));
	printf("oddBit(0x3): %X\n", oddBit(0x3));
	printf("oddBit(0x4): %X\n", oddBit(0x4));
	printf("oddBit(0xFFFFFFFF): %X\n", oddBit(0xFFFFFFFF));	
	printf("oddBit(0xAAAAAAAA): %X\n", oddBit(0xAAAAAAAA));
	printf("oddBit(0x55555555): %X\n", oddBit(0x55555555));
}
