#include <stdio.h>
#define UI unsigned int

UI extract(UI x, int i){
	UI aShift = i << 3; // multiply by 8
	UI aMask = 0xFF << aShift; // FF to FF000000

	UI ex  = x & aMask; // extract FF to get 78 or cd
	char sol = ex >> aShift; // padding this to get FFFFFF
	return sol;
}

int main() {
	printf("extract(0x12345678, 0): 0x%08X\n", extract(0x12345678, 0)); // the 08 is used to get 000000
	printf("extract(0xABCDEF00, 2): 0x%X\n", extract(0xABCDEF00, 2));
}
