#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "p1fxns.h"
#include <stdbool.h>
#define NUMBER 129

//setenv(“USPS_QUANTUM_MSEC”);

//getenv(“USPS_QUANTUM_MSEC”);

// section 3.10 CADS (page 131)

// for i in 0 .. numprograms-1
	// pid[i] = fork();
// if (pid[i] == 0)
	// prepare argument structure;
	// execvp(program[i], args[i])
// for i in 0 .. numprograms-1
	// wait(pid[i])
//child returns 0
//parent returns child's pid

// ^^ C code for the above pseudocode ^^


int main(int argc, char *argv[]) {
	int opt;
	char c;
	char *p;
	char *s;
	int fd;
	char *file_name = argv[argc-1];
	char buf[];
	int num_prog = 0;
	int USPS_QUANTUM_MSEC;
	char args[][];
	int j = 0;
	int k = 0;

	while ((opt = getopt(argc, argv, "1234")) != -1) {
		switch(opt) {
			case '1': 
			if (p = getenv("USPS_QUANTUM_MSEC") != NULL) {
				p1getline(STDIN_FILENO, buffer, 1024);	
			} else {
				exit(EXIT_FAILURE);
			}

			// part 2 open the file
			fd = open(file_name, argc);
			if (fd == -1) {
				exit(EXIT_FAILURE);
			}

			// part 3
			while (p1getline(fd, buffer, NUMBER) > 0) {
				num_prog++;

				while ((j = p1getword(buffer, j, args[k])) != -1) {
					if (args[i][0] == '\0') {
						break;
					}
					
					k++;
				}

				for (int i = 0; i < num_prog-1; i++) {
					int pid 
					pid[i] = fork();
					switch (pid[i]) {
						case -1: p1error(fd, s);
						goto wait_for_children;
						case 0: execvp(args[0], args);
						default: 

					}
				}

			}


			// part 4
			wait_for_children:
				for (i=0; i < num_prog-1; i++) {
					wait(&pid[i]);
					num_prog--;
				}

			case '2': 
			// part 1 deal with q flag
			if (p = getenv("USPS_QUANTUM_MSEC") != NULL) {
				p1getline(STDIN_FILENO, buffer, 1024);
			} else {
				exit(EXIT_FAILURE);
			}

			if (opt = getopt(argc, argv[1], "q") != -1) {
				USPS_QUANTUM_MSEC = argv[2];
			} else {
				exit(EXIT_FAILURE);
			}

			// part 2 open the file
			fd = open(file_name, argc);
			if (fd == -1) {
				exit(EXIT_FAILURE);
			}

			// part 3
			while (p1getline(fd, buffer, NUMBER) > 0) {
				num_prog++;

				while ((j = p1getword(buffer, j, args[k])) != -1) {
					if (args[i][0] == '\0') {
						break;
					}
					k++;
				}

				for (int i = 0; i < num_prog-1; i++) {
					int pid 
					pid[i] = fork();
					switch (pid[i]) {
						case -1: p1error(fd, s);
						goto wait_for_children;
						case 0: execvp(args[0], args);
						default:

					}
				}

			}
			
			// part 4
			wait_for_children:
				for (i=0; i < num_prog-1; i++) {
					wait(&pid[i]);
					num_prog--;
				}

			case '3': 
			if (p = getenv("USPS_QUANTUM_MSEC") != NULL) {
				p1getline(STDIN_FILENO, buffer, 1024);
			} else {
				exit(EXIT_FAILURE);
			}

			//part 2 open the file
			fd = open(file_name, argc);
			if (fd == -1) {
				exit(EXIT_FAILURE);
			}

			// part 3
			while (p1getline(fd, buffer, NUMBER) > 0) {
				num_prog++;

				while ((j = p1getword(buffer, j, args[k])) != -1) {
					if (args[i][0] == '\0') {
						break;
					}
					k++;
				}

				for (int i = 0; i < num_prog-1; i++) {
					int pid 
					pid[i] = fork();
					switch (pid[i]) {
						case -1: p1error(fd, s);
						goto wait_for_children;
						case 0: execvp(args[0], args);
						default:

					}
				}

			}


			// part 4
			wait_for_children:
				for (i=0; i < num_prog-1; i++) {
					wait(&pid[i]);
					num_prog--;
				}

			case '4':
			// part 1 deal with q flag
			if (opt = getopt(argc, argv[1], "q") != -1) {
				int q_m_sec = argv[2];
			} else {
				exit(EXIT_FAILURE);
			}

			// part 2 open file
			fd = open(file_name, argc);
			if (fd == -1) {
				exit(EXIT_FAILURE);
			}

			// part 3
			while (p1getline(fd, buffer, NUMBER) > 0) {
				num_prog++;

				while ((j = p1getword(buffer, j, args[k])) != -1) {
					if (args[i][0] == '\0') {
						break;
					}

					k++;
				}

				for (int i = 0; i < num_prog-1; i++) {
					int pid 
					pid[i] = fork();
					switch (pid[i]) {
						case -1: p1error(fd, s);
						goto wait_for_children;
						case 0: execvp(args[0], args);
						default:

					}
				}

			}

			// part 4
			wait_for_children:
				for (i=0; i < num_prog-1; i++) {
					wait(&pid[i]);
					num_prog--;
				}

			default: exit(EXIT_FAILURE);
		} 
	}

}

/*
int main(int argc, char *argv[]) {
	int opt;
	char c;
	char *p;
	int fd;
	char *file_name = argv[argc-1];
	char buf[BUFSIZE];
	char buffer[];


	if (argc == 1) {
		//default to standard input
		// is env var set?
		// if not abort
		// use it and check to see if the filepath is valid using open
		// if not, default to stdin
		// part 1 deal with q flag
		if (p = getenv("USPS_QUANTUM_MSEC") != NULL) {
			p1getline(STDIN_FILENO, buffer, 1024);
			close(fd);
		} else {
			return EXIT_FAILURE;
		}
		//part 2 open the file
		fd = open(file_name, argc);

		// part 3 arrange arguments, execvp


		//part 4 wait

	} else if (argc == 2) {
		//open workfile

		// part 1 deal with q flag
		if (p = getenv("USPS_QUANTUM_MSEC") != NULL) {
			p1getline(STDIN_FILENO, buffer, 1024);
			close(fd);
		} else {
			return EXIT_FAILURE;
		}
		//part 2 open the file
		fd = open(file_name, argc);
		
		// part 3 arrange arguments, execvp
		
		//part 4 wait

	} else if (argc == 3) {
		// check q flag

		// if yes, assign q_m_sec
		// move to stdin

		// part 1 deal with q flag
		if (opt = getopt(argc, argv[1], "q") != -1) {
			USPS_QUANTUM_MSEC = argv[2];
		}

		//part 2 open the file
		fd = open(file_name, argc);

		// part 3 arrange arguments, execvp
		
		//part 4 wait

	} else if (argc == 4) {
		// open workfile


		// part 1 deal with q flag
		if (opt = getopt(argc, argv[1], "q") != -1) {
			int q_m_sec = argv[2];
		else {
			return exit();
		}

		//part 2 open the file
			fd = open(file_name, argc);

			while (p1getline(fd, buffer, NUMBER) > 0) {
				num_prog++;

			}

			for (int i = 0; i < NUMBER-1; i++) {
				int pid 
				pid[i] = fork();
				switch (pid[i]) {
					case -1: //p1error
					case 0: //p1error
					default:

				}
			}
		}

		// part 3 arrange arguments, execvp
		
		//part 4 wait
	} else {
		// if argc > 4 (incorrect usage)
		return EXIT_FAILURE;
	}

	for (i=0; i < num_prog-1; i++) {
		wait(&pid[i]);
	}
}
*/

/* 
pt. 1
-deal with q flag
--is there a q flag use getopt to see if there is q flag
--if there is not a q flag, see if there is already environment variable of that name
--otherwise abort 

pt. 2
-open workfile
--use open command system call to open workfile
--if open was unsuccessful, abort

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


