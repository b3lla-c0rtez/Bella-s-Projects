#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#define UNUSED __attribute__((unused))
#define MAX 128


int main(UNUSED int argc, UNUSED char *argv[]) {
	char *args[MAX];

	args[0] = "echo";
	args[1] = "hello";
	args[2] = "world";
	args[3] = NULL;

	execvp(args[0], args);
	fprintf(stderr, "execvp() of 'echo hello world!' failed\n");
	return EXIT_FAILURE;
}
