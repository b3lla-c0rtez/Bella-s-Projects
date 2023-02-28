#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "ADTs/stack.h"

#define UNUSED __attribute__((unused))

void isPalindrome(FILE *fd, const Stack *st){
	char buf[BUFSIZ];
	printf("word - isPalin\n");
	while(fgets(buf, BUFSIZ, fd) != NULL) {
		int mid, i, N = strlen(buf);
		bool isPalindrome = true;

		if(buf[N-1] == '\n'){ buf[--N] = '\0'; }
		
		st->clear(st);
		mid = N / 2;

		for(i = 0; i < mid; i++) {
			st->push(st, ADT_VALUE((long)buf[i]));
		}	

		if((N%2)==1) { mid++; }

		for(i = mid; i < N; i++) {
			long value;
			st->pop(st, ADT_ADDRESS(&value));
			if((char) value != buf[i]){
				isPalindrome = false;
				break;
			}
		}
		printf("%s - %s\n", buf, (isPalindrome) ? "True" : "False");
	}
}

int main(UNUSED int argc, UNUSED char *argv[]){
	int exitStatus = EXIT_FAILURE;
	const Stack *st = Stack_create(doNothing);
	if(st == NULL){
		fprintf(stderr, "Unable to create stack. :C\n");
		goto exit;
	} else {
		isPalindrome(stdin, st);
		st->destroy(st);
		exitStatus = EXIT_SUCCESS;
	}
exit:
	return exitStatus;
}
