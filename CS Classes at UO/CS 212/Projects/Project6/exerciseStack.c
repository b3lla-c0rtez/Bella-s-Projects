#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "ADTs/stack.h"

#define UNUSED __attribute__((unused))

void printStack(const Stack *st, FILE *fp){
	void **decarray;
	long arrayint;
	int i;
		
	decarray = st->toArray(st, &arrayint);

	if(st->isEmpty(st)){
		printf("Empty\n");
	} else {
		for(i = 0; i < arrayint; i++) {
			if(i<arrayint-1) {
				fprintf(fp, "%ld " , (long)decarray[i]);
			} else {
				fprintf(fp, "%ld\n" , (long)decarray[i]);
			}
		}
	}
	free(decarray);
}

int main(UNUSED int argc, UNUSED char *argv[]) {
	int exitStatus = EXIT_FAILURE;
	const Stack *st = Stack_create(doNothing);

	if(st == NULL) {
		printf("Unable to create stack, :C\n");
		return exitStatus;
	} 
	
	FILE *fp;
	fp = fopen(argv[1], "r");

	char buf[BUFSIZ];
	long value;

	fgets(buf, BUFSIZ, fp);
	sscanf(buf, "%ld ",&value);

	for(int i = value; i > 0; i--){
		fgets(buf, BUFSIZ, fp);

		if ((strcmp(buf, "print\n")) == 0) {
			printStack(st, stdout);
		}

		else if ((strcmp(buf, "pop\n")) == 0) {
			long address;
			if(! st->pop(st, ADT_ADDRESS(&address))) {
				printf("StackError\n");
			} else {
				printf("%ld\n", address);
			}
		
		} else {
			long p;
			sscanf(buf+5, "%ld ", &p);
			st->push(st, ADT_VALUE(p));
		}
	}
	
	
	st->destroy(st);
	fclose(fp);
	exitStatus = EXIT_SUCCESS;
	return exitStatus;
}
