#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void prefixCat (FILE *fd, bool ifI, bool ifF) {
	int i = 0;
	char buf[BUFSIZ];
	char prefix [50] = "";

	if(!ifF) {printf(">>> "); }
	while(fgets(buf, BUFSIZ, fd) != NULL) {
		if(strcmp("q\n", buf) == 0) {
			break;
		} else{
			if(ifI) {
				sprintf(prefix, "%4d: ", i);
				i++;
			}
			printf("%s%s\n", prefix, buf);
		}
		if(!ifF) {printf(">> ");}
	}
	printf("Goodbye!\n");
}

int main (int argc, char *argv[]) {
	int option;
	extern int opterr;
	bool ifF, ifI;
	int exitStatus;
	bool start = true;
	char *filename;

	opterr = 0;
	ifI = ifF = false;
	while((option = getopt(argc, argv, "f:i")) != -1) {
		switch(option) {
			case 'i': ifI = true; break;
			case 'f': ifF = true; filename = optarg; break;
			default:
				 printf("Unknown flag: -%c\n", optopt);
				 start = false;
				 break;
			}
	}

	if(start) {
		if(ifF) {
			FILE *fd = fopen(filename, "r");
			if(fd == NULL) {
				fprintf(stderr, "Unable to open file: %s\n", filename);
				exitStatus = EXIT_FAILURE;
			} else {
				prefixCat(fd, ifI, ifF);
				fclose(fd);
			}
		} else {
			prefixCat(stdin,ifI, ifF);
		}
		exitStatus = EXIT_SUCCESS;
	} else {
		exitStatus = EXIT_FAILURE;
	}
	return exitStatus;
}
