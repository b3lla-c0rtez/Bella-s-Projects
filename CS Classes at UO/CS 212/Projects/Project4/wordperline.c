#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "ADTs/stringADT.h"
#include "ADTs/arraylist.h"
#define USAGE "usage: %s [-lp] [FILE] ...\n"

/*
 *this code only takes in up to 50 file pointers for the array. 
 */

void func(FILE *fd, bool ifL, bool ifP) {
	int i;
	const String *st = String_create("");
	char buf[BUFSIZ];

	while(fgets(buf, BUFSIZ, fd) != NULL) {
		st->clear(st);
		st->append(st, buf);
		
		if(ifL) {
			st->lower(st);
		}

		if(ifP) {
			st->translate(st, "[:punct:]", ' ');
		}
		
		const ArrayList *al = st->split(st, "");

		if(al == NULL) {
			continue;
		} else {

			for(i=0; i < al->size(al); i++){
				char *temp;
				(void) al->get(al, i, (void**)&temp);
				printf("%s\n", temp);
			}
		}
		
		al->destroy(al);
				
	}
	st->destroy(st);
}


int main(int argc, char *argv[]) {
	int opt;
	int nFiles = 0;
	FILE *fds[50]; 
    	bool ifL, ifP;
	extern int opterr;
	int exitStatus = EXIT_FAILURE;

	opterr = 0;
    	ifL = ifP = false;
	while((opt = getopt(argc, argv, "lp")) != -1){
		switch(opt){
            		case 'l': ifL = true; break;
			case 'p': ifP = true; break;
			default:
				fprintf(stderr, "%s: invalid option: %c\n", argv[0], optopt);
				fprintf(stderr, USAGE, argv[0]);
				goto cleanup;
		}
	}

	if((argc - optind) == 0) {
		func(stdin, ifL, ifP);
		exitStatus = EXIT_SUCCESS;
		goto cleanup;
	} else {
		int i;
		for(i =optind; i<argc; i++){
			FILE *fd = fopen(argv[i], "r");
			if(fd == NULL){
				fprintf(stderr, "%s: unable to open file: %s\n", argv[0], argv[i]);
				goto cleanup;
			}
			fds[nFiles++] = fd;
		}
		for(i=0; i<nFiles; i++){
			func(fds[i], ifL, ifP);
		}
		exitStatus = EXIT_SUCCESS;
		
	}

cleanup:
	for(int i=0; i<nFiles; i++){
		fclose(fds[i]);
	}
return exitStatus;

}



