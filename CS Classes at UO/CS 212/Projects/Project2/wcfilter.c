#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stsplit.h"
#define UNUSED __attribute__((unused))

void countLWC(FILE *fd, long *nl, long *nw, long *nc){
	long nlines = 0L;
	long nwords = 0L;
	long nchar = 0L;
	
	char buf[BUFSIZ];
	while (fgets(buf, BUFSIZ, fd) != NULL) {
		nlines++;
		nchar += strlen(buf);

		char **wordcnt = stsplit(buf);
		for (int w = 0; wordcnt[w] != NULL; w++)
			nwords++;

		stfree(wordcnt);
	}
	
	*nl = nlines;
	*nw = nwords;
	*nc = nchar;
	
}

int main(UNUSED int argc, UNUSED char *argv[]){
	int exitStatus = EXIT_SUCCESS;

	long nl;
	long nw;
	long nc;

	countLWC(stdin, &nl, &nw, &nc);

	printf("%8ld", nl);
	printf("%8ld", nw);
	printf("%8ld\n", nc);

	return exitStatus;
}

