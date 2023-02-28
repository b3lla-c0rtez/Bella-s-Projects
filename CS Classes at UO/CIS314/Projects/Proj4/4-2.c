#include <stdio.h>

long fact(long x) {
	if (x <= 1) {
		return 1;
	}
	return x * fact(x-1);
}

int main() {
	printf("fact(1): %ld\n", fact(1));
	printf("fact(3): %ld\n", fact(3));
	printf("fact(5): %ld\n", fact(5));
}

// x86-64 instructions that modify the stack pointer:
// fact:
// call fact - call adds 8
// pushq %rbx
// popq %rbx
// ret - clears the stack
//
//.L3
// ret
//
// size of stack frame (size of int pointer): 4 bytes
