#include <stdio.h>
#define N 4
typedef long array_t[N][N];

void transpose(array_t a) {
	for (long i = 0; i<N; ++i){
		for (long j = 0; j<i; ++j) {
			long t1 = a[i][j];
			long t2 = a[j][i];
			a[i][j] = t2;
			a[j][i] = t1;
		}
	}
}

// .L3
// movq (%rax), %rcx is t1
// movq (%rdx), %rsi is t2
// movq %rsi, (%rax) is a
// movq %rcx, (%rdx) is A
// addq $8, %rax is N
// addq $32, %rdx is N
// cmpq %r9, %rax is for loop; j<i
// jne .L3 is for loop; j<i
// help from Linette on Transpose Opt

void transposeOpt(array_t a) {

	for (long i = 0; i<N; i++) {
		long *index1 = &a[i][0]; // index1 is a pointer is a pointer for the row
		long *index2 = &a[0][i]; //index2 is a pointer is a pointer for the collumn

		for (long j = 0; j < i; j++) { //dereference in this loop
			long t1 = *index1; // sets temp var t1 to index1
			long t2 = *index2; // sets temp var t2 to index2
			*index1 = t2; // swaps index1 to t2
			*index2 = t1; // swaps index2 to t1
			index1 ++; // move index1 to next column
			index2 += N; // move index2 to row

		}
	}
}

// help from Arturo Diaz with void printarr and main function

void printarr(array_t a) {
	for(int columns = 0; columns <= 3; columns++) {
		for(int rows = 0; rows<=3; rows++) {
			printf("%ld ", a[columns][rows]);
		}
	printf("\n");
	}
}

int main() {
	array_t a = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
	printarr(a); 
	printf("\nTranposeOpt:\n");
	transposeOpt(a);
	printarr(a);
}
