#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <math.h>
#include "ADTs/stringADT.h"
#include "ADTs/arraylist.h"

#define USAGE "usage: %s [-p] [FILE] ..."

void func(FILE *fd) {
	int i;
	const ArrayList *csv = ArrayList_create(0L, NULL);
	const String *st = String_create("");
	char buf[BUFSIZ];
	while(fgets(buf, BUFSIZ, fd) != NULL) {
		st->clear(st);
		st->append(st, buf);
		const ArrayList *al = st ->split(st, ",");
		printf("\nLooping with iterator\n");
		const Iterator *it = al->itCreate(al);
		while(it->hasNext(it)) {
			char *temp;
			(void) it->next(it, (void **)&temp);
			printf("|%d|\n", atoi(temp));
		}
		printf("\nLooping with indexing\n");
		for (i=0; i < al->size(al); i++) {
			char *temp;
			(void) al->get(al, i, (void**)&temp);
			printf("|%d|\n", atoi(temp));
		}
		al->destroy(al);
		it->destroy(it);

	}
	st->destroy(st);	
	csv->destroy(csv);
}

int main(int argc, char *argv[]) {
	int opt;
	int nFiles = 0;
	FILE *fds[50];
	bool printFile = false;
	extern int opterr;
	int exitStatus = EXIT_FAILURE;

	opterr = 0;
	while((opt = getopt(argc, argv, "p")) != -1){
		switch(opt){
			case 'p':
				printFile = true; break;
			default:
				fprintf(stderr, "%s: invalid option: %c\n", argv[0]);
				fprintf(stderr, USAGE, argv[0]);
				goto cleanup;
		}
	}

	if((argc - optind) == 0) {
		fprintf(stderr, USAGE, argv[0]);
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
		if(printFile) {	
			for(i = 0; i<nFiles; i++){
				func(fds[i]);
            }
		}
		exitStatus = EXIT_SUCCESS;
	}

cleanup:
	for(int i=0; i<nFiles; i++){
		fclose(fds[i]);
	}
return exitStatus;

}
