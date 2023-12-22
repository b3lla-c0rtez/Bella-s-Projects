#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#define UNUSED __attribute__((unused))

int main(UNUSED int argc, UNUSED char *argv[]) {
	/*  both  */
	pid_t id;
	id = fork();

	switch(id){
		case -1: fprintf(stderr, "fork called fail.\n");
			return EXIT_FAILURE;
		case 0: 
			printf("Child: pid %d, Parent PID %d\n", getpid(), getppid());
			break;
		default:
			printf("Parent: pid %d, child %d\n", getpid(), getppid());
			wait(NULL);
			break;
	}

	return EXIT_SUCCESS;
}
