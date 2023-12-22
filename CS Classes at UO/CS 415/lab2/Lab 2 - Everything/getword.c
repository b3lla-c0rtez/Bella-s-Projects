#include "p1fxns.h"
#include <stdlib.h>
#define UNUSED __attribute__((unused))

int main(UNUSED int argc, UNUSED char *argv[]) {
	char buf[4096], word[4096];
	//A file descriptor is a unique identifier that represents an open file or 
	//input/output (I/O) device within a process in Unix-like operating systems.
	//standard input (file descriptor 0)
	//standard output (file descriptor 1)
	//In simple terms, a file descriptor is like a special code that helps a 
	//program talk to a file or some other thing that it needs to read or write from.
	while (p1getline(0, buf, sizeof buf) != 0) {
		int i = p1strchr(buf, '\n');
		buf[i] = '\0';
		i = 0;
		p1putstr(1, "|");
		while ((i = p1getword(buf, i, word)) != -1) {
			p1putstr(1, word);
			p1putstr(1, "|");
		}
		p1putstr(1, "\n");
	}
	return EXIT_SUCCESS;
}
