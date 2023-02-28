#include <stdio.h>

// original C function:
//
// int sumArr(long *a, long size) {
//   long result = 0;
//   for (long i = size - 1; i >= 0; --i) {
//     result += a[i];
//   }
//   return result;
// }
//
// assembly: your implementation below

long sumArr(long *a, long size) {
        // Declare and initialize result var – do not modify.
        long result = 0;

        // Ensure that argument *from* is in %rdi,
        // argument *to* is in %rsi, *result* is in %rax - *do
        // not modify*.
        __asm__ ("movq %0, %%rdi # from in rdi;" :: "r" ( a ));
        __asm__ ("movq %0, %%rsi # to in rsi;" :: "r" ( size ));
        __asm__ ("movq %0, %%rax # result in rax;" :: "r" ( result ));

        // Your x86-64 code goes below - comment each instruction...
        __asm__(
                // TODO - Replace the two lines below with add, compare,
                // jump instructions, labels, etc as necessary to implement
                // the loop.
		// comment each line explaining its purpose

                "subq $1, %rsi;" // long i = size - i
	       // we're given n, want to loop from n-1 to 0	
                ".LOOP:" // for loop start label
                "cmpq $-1, %rsi;" // check if i == -1 (effectively i >= 0)
                "je .END;" // jump if previous instruction set equal to flag to 1
		// if we don't jump, fall through
		// 4, 3, 2, 1, 0; stop at -1 (i >= 0 is not true)	
                "addq (%rdi, %rsi, 8), %rax;" // result += a[i]
		//generate formula: base, size, offset (roughly)
		// (a, b, c), d evaluates to d += a+c*b
		// specifically we have: rax += rdi + 8*rsi

		// rdi holds the pointer value to a[0]
		// rsi holds the value of i
		// so 8*rsi gives a[i]
		// for example a[4] would be %di + 8*4 = %rdi + 32 (move right by 32 bits = 4 long)

                "subq $1, %rsi;" //--i 
                "jmp .LOOP;"
                ".END:"
        );

        // Ensure that *result* is in %rax for return - *do not modify*.
        __asm__ ("movq %%rax, %0 #result in rax;" : "=r" ( result ));
        return result;
}

int main() {
        long testArr[5] = {1, 2, 3, 4, 5};
        printf("sumArr({1, 2, 3, 4, 5}, 5): %ld\n", sumArr(testArr, 5));
}
