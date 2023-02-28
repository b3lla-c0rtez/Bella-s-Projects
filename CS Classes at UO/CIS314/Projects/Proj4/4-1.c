// long sum(long from, long to) {
// 	long result = 0;
// 	loop:
// 		result += from;
// 		++from;
// 		if(from<=to) goto loop;
// 		return result;
// }

#include <stdio.h>
long sum(long from, long to) {
	// declare and intialize result var
	long result = 0;
	// ensure that argument *from* is in %rdi
	// argument *to* is in %rsi, *result* is in %rax
	
	__asm__ ("movq %0, %%rdi # from in rdi;" :: "r" ( from ));
	__asm__ ("movq %0, %%rsi # to in rsi;" :: "r" ( to ));
	__asm__ ("movq %0, %%rax # result in rax;" :: "r" ( result ));

	__asm__(
		".L2:" // loop
		"addq %rdi, %rax;" // result += from (result plus to)
		"addq $1, %rdi;" // ++from (adding from)
		"cmpq %rsi, %rdi;" // comparing from and to 
		"jle .L2;" // if from is less than or equal to jump to loop
	);

	__asm__("movq %%rax, %0 #result in rax;" : "=r" ( result ));
	return result;
}

int main() { 
	printf("sum(1,6): %ld\n", sum(1,6));
	printf("sum(3,5): %ld\n", sum(3,5));
	printf("sum(5,3): %ld\n", sum(5,3));
}
