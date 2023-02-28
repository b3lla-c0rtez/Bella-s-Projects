#include "ADTs/hashcskmap.h"
#include "ADTs/stringADT.h"
#include "ADTs/arraylist.h"
#include "sort.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void helpfunc(FILE *fd, bool ifA, bool ifF, bool ifI, bool ifL, bool ifP) {
	int i;
	const String *st = String_create("");
	char buf[BUFSIZ];
	const CSKMap *m = HashCSKMAP(0L, 0.0, freeValue);

	while (fgets(buf, BUFSIZ, fd) != NULL) {
		st->clear(st);
		st->append(st, buf);

		if(ifL) {
			st->lower(st);
		}

		if(ifP) {
			st->translate(st, "[:punct:]", ' ');
		}
	
		const ArrayList *al = st->split(st, "");

		if(ifA) {
		
		}

		if(ifF) {
		
		}

		if(ifL) {
			if(ifA) {
			
			}

			if(ifP) {
			
			}
		}	
	}
}

int main(int argc, char *argv[]) {
	int opt;
	int nFiles = 0;
	FILE *fds[50];
	bool ifA, ifF, ifI, ifL, ifP;
	extern int opterr;
	int exitStatus = EXIT_FAILURE;

	opterr = 0;
	ifA = ifF = ifI = ifL = ifP = false;
	while((opt = getopt(argc, argv, "afilp")) != -1) {
		switch(opt){
			case 'a': ifA = true; break;	  
			case 'f': ifF = true; break;
			case 'i': ifI = true; break;
			case 'l': ifL = true; break;
			case 'p': ifP = true; break;
			
			default:
				  fprintf(stderr, "%s: invalid option: %c\n", argv[0], optopt);
				  fprintf(stderr, USAGE, argv[0]);
				  goto cleanup;
		}
	}

	if((argc-optind) == 0) {
		helpfunc(stdin, ifA, ifF, ifI, ifL, ifP);
		exitStatus = EXIT_SUCCESS;
		goto cleanup;
	} else {
		int i;
		for(i = optind; i<argc; i++) {
			FILE *fd = open(argv[i], "r");
			if(fd == NULL) {
				fprintf(stderr, "%s: unable to open file %s\n" ,argv[0], argv[i]);
				goto cleanup;
			}
			fds[nFiles++] = fd;
		}
		for(i=0; i<nFiles; i++){
			helpfunc(fds[i], ifA, ifF, ifI, ifL, ifP);
		}
		exitStatus = EXIT_SUCCESS;
	}
	
cleanup:
	for(int i=0; i<nFiles; i++){
		fclose(fds[i]);
	}

return exitStatus;

}
