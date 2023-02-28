#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define UNUSED __attribute__((unused))

int main(UNUSED int argc, UNUSED char *argv[]){
	char buf[BUFSIZ];
	char last[BUFSIZ] = "";
	int  nlines = 1;
	
	while(fgets(buf, BUFSIZ, stdin) != NULL) {
		if(strcmp(buf, last) != 0) {
			printf("%7d", nlines); printf(" "); printf(last);
			strcpy(last, buf);
			nlines = 1;
		} else {
			nlines++;
		}
	}
	printf("%7d", nlines); printf(" "); printf(last);
}
