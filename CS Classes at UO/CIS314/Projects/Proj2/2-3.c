#include <stdio.h>
#define UI unsigned int

int le(float x, float y) {
	unsigned int ux = *((unsigned int*) &x); // convert x bits
	unsigned int uy = *((unsigned int*) &y); // convert y bits
	unsigned int sx = ux >> 31; // extract bit ux
	unsigned int sy = uy >> 31; // extract bit uy
	ux <<= 1; // drop sign bit of ux
	uy <<= 1; // drop sign bit of uy
	UI cas1 = ((ux == uy) && (sx == sy));// if signs and values are same
	UI cas2 = ((sx == 0) && (sy == 0) && (uy >= ux)); // if signs are same(pos) and y value >= x value
	UI cas3 = ((sx == 1) && (sy == 1) && (ux >= uy)); // if signs are same(neg) and x value >= y value
	UI cas4 = ((sx == 1) && (sy == 1) && (ux == uy)); // if signs are same(neg) and x value and y value are same
	UI cas5 = ((ux == 0) && (uy == 0)); // if values are same
	UI cas6 = ((sx == 1) && (sy == 0)); // if signs are different
	return   cas1 || cas2 || cas3 || cas4 || cas5 || cas6;

}

int main() {
	printf("le(0.0f, 0.0f): %d\n", le(0.0f, 0.0f));
	printf("le(-0.0f, 0.0f): %d\n", le(-0.0f, 0.0f));
	printf("le(-1.0f, 1.0f): %d\n", le(-1.0f, 1.0f));
	printf("le(1.0f, 1.0f): %d\n", le(1.0f, 1.0f));
	printf("le(-1.0f, 0.0f): %d\n", le(-1.0f, 0.0f));
	printf("le(0.0f, 1.0f): %d\n", le(0.0f, 1.0f));
	printf("le(1.0f, 0.0f): %d\n", le(1.0f, 0.0f));
	printf("le(0.0f, -1.0f): %d\n", le(0.0f, -1.0f));
	printf("le(-1.0f, -2.0f): %d\n", le(-1.0f, -2.0f));
}
