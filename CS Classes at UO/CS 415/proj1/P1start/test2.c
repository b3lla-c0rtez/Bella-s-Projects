#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "p1fxns.h"
#include <stdbool.h>
#define NUMBER 129

int main(int argc, char *argv[]) {
	fprintf(stdout, "argc: %d\n", argc);
	for (int i =0; i < argc; i++) {
		fprintf(stdout, "argv[%d]\t%s\n", i, argv[i]);
	}
}