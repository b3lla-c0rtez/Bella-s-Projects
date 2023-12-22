#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "p1fxns.h"
#include <stdbool.h>
#include <stdint.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <sys/time.h>
#include <unistd.h>
#include <fcntl.h>

/* 
pt. 3
-arrange arguments and loop
--pseuodocode starts here
--begin loop as long as there is line to read
---put line into character buffer (string/char [])
---take each word of line and put into array of strings (from char buffer to array of strings)
---fork, save pid to pid array in parent
---in child, execvp(array of strings[0], array of strings)

pt. 4
-in parent, loop through each pid and wait
*/
volatile bool isHandling = false; // creating volatile (using it in sigal) bool and setting equal to false; both

void handle_sigusr1(int signal) {
	isHandling = true; // changing the boolean varible to true, when signal is sent; both
}

int main(int argc, char *argv[]) {
	struct timespec ms20 = {0, 20000000}; // setting time up to use in nanosleep; both
	signal(SIGUSR1, handle_sigusr1); // subscribing to signal to make sure we get the signal; both
	pid_t pid = fork(); // forks parent process, creates child procress

	if (pid == 0) { // checks if child
		fprintf(stdout, "i hope this works\n"); 
		while(!isHandling) { // while isHandling is false, then child sleeps for 20ms
			nanosleep(&ms20, NULL); // child sleeps
		}
		execvp(argv[1], &argv[1]); // if not sleeping it does execvp
	}
	fprintf(stdout, "about to send signal\n");
	kill(pid, SIGUSR1); 
	fprintf(stdout, "signal sent\n");
	fprintf(stdout, "stopping signal\n");
	kill(pid, SIGSTOP);
	fprintf(stdout, "continuing signal\n");
	kill(pid, SIGCONT);
	fprintf(stdout, "about to wait\n");
	wait(&pid);
	fprintf(stdout, "done waiting\n");
}