#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "ADTs/stack.h"

#define UNUSED __attribute__((unused))

void printStack(FILE *fp, const Stack *st) {	
	char exp[BUFSIZ];
	long value;
	//bool match = false;
	//int num;

	fgets(exp, BUFSIZ, fp);
	sscanf(exp, "%ld ", &value);

	while(fgets(exp, BUFSIZ, fp) != NULL) {

		int lenofline = strlen(exp);
		int i; 

		bool printStack = true;

		for(i = 0; i < lenofline - 1; i++) {
			char open[] = "({[<"; 
			char close[] = ")}]>";

			if(strchr(open, exp[i]) != NULL) {
				st->push(st,(void*)(long)exp[i]);
			} else {
				long p;
				st->pop(st,(void **)&p);
				
				bool match = false;
				int num;

				for(num = 0; num < 4; num++){
					if(close[num] == exp[i]) {
						break;
					}
				}
				if(open[num] == p) {
					match = true;
				}
	
				if(!match) {
					printStack = false;
					break;
				}
			}
		}

		if(st->isEmpty(st) && printStack) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
		
		st->clear(st);	
	}
}

int main(UNUSED int argc, UNUSED char *argv[]) {	
	int exitStatus = EXIT_FAILURE;
	const Stack *st = Stack_create(doNothing);

	if(st == NULL) {
		printf("Unable to create stack, :C\n");
		return exitStatus;
	} else {
		FILE *fp;
		fp = fopen(argv[1], "r");

		printStack(fp, st);

		st->destroy(st);

		exitStatus = EXIT_SUCCESS;
	}

	return exitStatus;
}
/*
 *declare character stack
 *
 *
 *traverse
 *
 *
 *if start bracket is (, [, {, push
 *
 *
 *if end bracket is ), ], }, pop
 *
 *
 * if pop matches start, then ok
 *
 *
 *else, not balanced
 *
 *
 *after traversal, not balanced
 *
 */

