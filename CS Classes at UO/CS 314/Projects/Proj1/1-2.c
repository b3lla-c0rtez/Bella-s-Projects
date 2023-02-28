#include <stdio.h>
#define UI unsigned int

UI replace(UI x, int i, unsigned char b) {
	UI xShift = i << 3; //multiply by eight; three*eight = twenty-four ... if i was three, the location is twenty-four
	UI aMask = 0xFF << xShift; //FF to FF000000

	UI extract = x & ~aMask; //extracting FF to get 345678 or 123456
	extract |= b << xShift; // aligning b and doing replace action
	return extract; //returning result

	
}

int main() {
	printf("replace(0x12345678, 3, 0xAB): %X\n", replace(0x12345678, 3, 0xAB));
	printf("replace(0x12345678, 0, 0xAB): %X\n", replace(0x12345678, 0, 0xAB));
}
