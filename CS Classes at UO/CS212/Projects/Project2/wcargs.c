#include <stdio.h>
#include <unistd.h>
#include <stdbool.h>
#include <stdlib.h>
#define USAGESTR "usage: %s [-123] FILE1 FILE2\n"

int main(int argc, char *argv[]) {
	int option;
	extern int opterr;
	bool lcount, wcount, ccount;
	char *filename;
	int nOptions = 0;
	
	lcount = wcount = ccount = false;
	opterr = 0;
	while((option = getopt(argc, argv, "lwc")) != -1) {
		switch(option){
			case 'l': lcount = true; nOptions++; break;
			case 'w': wcount = true; nOptions++; break; 
			case 'c': ccount = true; nOptions++; break;
			default: fprintf(stderr, "%s: illegal option, '-%c\n", argv[0], optopt);
				 fprintf(stderr, USAGESTR, argv[0]);
				 return EXIT_FAILURE;
		}

	}

	if((lcount == false) && (wcount == false) && (ccount == false))
		lcount = wcount = ccount = true;

	if(lcount)
		printf("Counting lines\n");

	if(wcount)
		printf("Counting words\n");

	if(ccount)
		printf("Counting characters\n");

	int x = argc-optind;
	if(x == 0)
		printf("Processing standard input and no total line\n");

	if(x == 1){
		filename=argv[optind];
		printf("Processing %s and no total line\n", filename);
	}
	if(x > 1){
		printf("Processing");
		for (int i= optind;i<argc-1;i++) 
			printf(" %s,",argv[i]);
		

		printf(" %s and a total line\n",argv[argc-1]);

	}
	
	return EXIT_SUCCESS;
}
