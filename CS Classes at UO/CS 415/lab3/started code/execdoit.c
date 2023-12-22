#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

void printargs(char *prefix, char *argv[], char *suffix) {
	int i;
	fprintf(stderr, "%s", prefix);
	for (i=0; argv[i] !=NULL; i++) {
		fprintf(stderr, "%s", argv[i]);
	}
	fprintf(stderr, "%s\n", suffix);
}

int main(int argc, char *argv[]) {
	printargs("attempting to execvp()", argv+1, "");
	execvp(argv[1], argv+1);
	printargs("execvp() of ' ", argv+1, "'failed");

	return EXIT_FAILURE;
}
