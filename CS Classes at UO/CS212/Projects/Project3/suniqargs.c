#include <string.h>
#include <unistd.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#define USAGESTR "usage: %s [-123] FILE1 FILE2\n"

int main(int argc, char *argv[]) {
	int option;
	extern int opterr;
	bool numOccur, dupLines, casCmp, uniLines;
	char *filename;
	int nOptions;
	
	numOccur = dupLines = casCmp = uniLines = false;
	opterr = 0;
	while((option = getopt(argc, argv, "cdiu")) != -1){
		switch(option) {
			case 'c': numOccur = true; nOptions++; break;
			case 'd': dupLines = true; nOptions++; break;
			case 'i': casCmp = true; nOptions++; break;
			case 'u': uniLines = true; nOptions++; break;
			default: fprintf(stderr, "%s: illegal option, '-%c\n", argv[0], optopt);
				 fprintf(stderr, USAGESTR, argv[0]);
				 return EXIT_FAILURE;
		}

	}
	
	if((numOccur == false) && (dupLines == false) && (casCmp == false) && (uniLines == false))
		numOccur = dupLines = casCmp = uniLines = true;

	if(numOccur)
		printf("Prefix lines by number of occurences\n");

	if(dupLines)
		printf("Only print duplicate lines\n");

	if(casCmp)
		printf("Ignore case differences\n");

	if(uniLines)
		printf("Only print unique lines\n");


	int x = argc-optind;
	if(x == 0)
		printf("Processing standard input and no total line\n");

	if(x == 1){
		filename = argv[optind];
		printf("Processing %s \n", filename);		
	}

	return EXIT_SUCCESS;
}
