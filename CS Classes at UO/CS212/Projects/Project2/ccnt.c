#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define UNUSED __attribute__((unused))

int main(UNUSED int argc, UNUSED char *argv[]){
	long nchar = 0L;
	char buf[BUFSIZ];
	int exitStatus = EXIT_SUCCESS;

	while (fgets(buf, sizeof buf, stdin) != NULL) {
		nchar += strlen(buf);
	}
	printf("%8ld\n", nchar);
	return exitStatus;
}
