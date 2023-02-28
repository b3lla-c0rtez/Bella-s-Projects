#include <stdio.h>

void printBytes(unsigned char *start, int len) {
	for (int i=0; i<len; ++i) {
		printf(" %.2x", start[i]);
	}
	printf("\n");
}

void printInt(int x) {
	printBytes((unsigned char *) &x, sizeof(int));
}

void printFloat(float x) {
	printBytes((unsigned char *) &x, sizeof(float));
}

void printShort(short x) {
	printBytes((unsigned char *) &x, sizeof(short)); //printing short
}

void printLong(long x) {
	printBytes((unsigned char *) &x, sizeof(long)); //printing long (32-bits)
}

void printLongLong(long long x) {
	printBytes((unsigned char *) &x, sizeof(long long));//printing long long (64 bits)
}

void printDouble(double x) {
	printBytes((unsigned char *) &x, sizeof(double));//printing double
}

int main() { 
	printInt(156); //int representation of 156 is 9c 00 00 00; this makes sense because int is between the short and long
	printFloat(15.6); //float representation, 15.6 is a float and it is 9a 99 79 41
	printShort(156); //short representation of 156 holds least amount; it is 9c 00
	printLong(156); //the long representation of 156 is 9c 00 00 00 00 00 00 00 00 (makes sense because it holds 32 bits)
	printLongLong(1800); //the long long representation of 1800 is 08 07 00 00 00 00 00 00
	printDouble(4.8); //the double representation of 4.8 is 33 33 33 33 33 33 13 40
	//I notice this is the result:
	//9c 00 00 00
	//9a 99 79 41
	//9c 00
	//9c 00 00 00 00 00 00 00
	//08 07 00 00 00 00 00 00
	//33 33 33 33 33 33 13 40
	//The result is printing the value of each type as a byte in (hex).The ordering is based on Debian being a Linux operating system as well as the byte adress. 
	//The number 156 is being represented in 3 different ways, first an int, then short, then long, then double.
	//for the float it is represented as 15.6; 15.6 is represented in this way only (used .6 since it is a float)
	//for the long long it is represented as 1800 because it can hold more than ints, shorts, and longs; 1800 is represented in this way only
	//for the double, it is represented as 14.8 because it can be an integer or a decimal; 14.8 is represented once 
}
