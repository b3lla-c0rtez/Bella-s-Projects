#include <stdio.h>

long f(long x, long y, long z) {
	long t1 = z+y; // deq + src
	long t2 = x*t1; // deq*src
	long t3 = t2<<63; //deq<<src
	long t4 = t3>>63; //deq>>src
	long rval = t2^t4; //deq^src
	return rval;
}

int main() {
	printf("f(1, 2, 4): %ld\n", f(1, 2, 4));
	printf("f(3, 5, 7): %ld\n", f(3, 5, 7));
	printf("f(10, 20, 30): %ld\n", f(10, 20, 30));
}
