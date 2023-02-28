#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <strings.h>

void printLine(char *line, int count, bool ifC, bool ifD, bool ifU) {
	if(ifD && count>1 && !ifU) {
		if(ifC){
			printf("%7d %s",count, line);	
		}

		else {
			printf("%s", line);
		}

	}	

	if(!ifD && count== 1 && ifU) {
		if(ifC) {
			printf("%7d %s",count, line);
		}

		else {
			printf("%s", line);
		}
	}

	if(!ifD && !ifU) {
		if(ifC) {
			printf("%7d %s",count, line);
		}

		else {
			printf("%s", line);
		}
	}
}

void uniqFile (FILE *fd, bool ifC, bool ifD, bool ifI, bool ifU) {
	int count = 1;
	char buf[BUFSIZ];
	char last[BUFSIZ];
	fgets(buf,BUFSIZ,fd);

	while(fgets(last, BUFSIZ, fd) != NULL) {
		if(ifI){
			if(strcasecmp(buf,last)==0){
				count++;
			}
			else{
				printLine(buf,count,ifC,ifD,ifU);
				strcpy(buf, last);
				count = 1;
			}
		}
		else {
			if(strcmp(buf, last) == 0) {
				count++;
			}
			else{
				printLine(buf,count,ifC,ifD,ifU);
				strcpy(buf, last);
				count = 1;

			}

		}

	}
printLine(buf, count, ifC, ifD, ifU);
}

int main(int argc, char *argv[]) {
	int option;
	extern int opterr;
	bool ifC, ifD, ifI, ifU;
	int exitStatus;
	bool start = true;

	opterr = 0;
	ifC = ifD = ifI = ifU  = false;
	while((option = getopt(argc, argv, "cdiu")) != -1) {
		switch(option){
			case 'c': ifC = true; break;
			case 'd': ifD = true; break;
			case 'i': ifI = true; break; 
			case 'u': ifU = true; break;
			
			default:
				 printf("Unknown flag: -%c\n", optopt);
				 start = false;
				 break;
		}
	}

	if(start) {
		if(argc == optind){
			uniqFile(stdin, ifC, ifD, ifI, ifU);
		} else if(argc - optind == 1){
			FILE *fd = fopen(argv[optind], "r");
			if(fd == NULL) {
				fprintf(stderr, "Unable to open file: %s\n", argv[optind]);
				exitStatus = EXIT_FAILURE;
			} else {
				uniqFile(fd, ifC, ifD, ifI, ifU);
				fclose(fd);
				exitStatus = EXIT_SUCCESS;
			}
		} else {
			fprintf(stderr, "Usage: ./suniq [OPTION] ... [FILE] \n");
		}
	} else {
		exitStatus = EXIT_FAILURE;
	}
	return exitStatus;
}
