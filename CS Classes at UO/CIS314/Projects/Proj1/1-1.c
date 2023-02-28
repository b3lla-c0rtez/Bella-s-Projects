#include <stdio.h>
#define UI unsigned int
UI combine(UI x, UI y) {
	UI xMask = 0b11111111111111111111111100000000; //32 bit mask; 1s are the values of one-six and a-f that are wanted, 0s are the last two values we don't want to keep
	UI yMask = 0b00000000000000000000000011111111; //32 bit mask; 0s are the values that we don't want in the combine, 1s are the values we want in the combine for the two end values

	UI a = xMask & x; //extracting x-bits and applying it to x
	UI b = yMask & y; //extracting y-bits and it applying it to y

	UI result = a ^ b; //combining the extracted bits

	return result;
}

int main() {
	printf("combine(0x12345678, 0xABCDEF00): %X\n",  combine(0x12345678, 0xABCDEF00));
	printf("combine(0xABCDEF00, 0x12345678): %X\n", combine(0xABCDEF00, 0x12345678));

}
