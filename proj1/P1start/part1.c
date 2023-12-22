#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/* 
pt. 1
-deal with q flag
--is there a q flag use getopt to see if there is q flag
--if there is not a q flag, see if there is already environment variable of that name
--otherwise abort 
*/

int main(int argc, char *argv[]) {
	char *qvalue = NULL;
	int opt;

	while ((opt = getopt(argc, argv, "q:")) != -1) {
		if (opt == 'q') {
			printf("it worked\n");
		} else {
			printf("error\n");
		}
		// switch(opt) {
			// case 'q': fprintf(stdout, "it worked\n"); 
			// case '?': fprintf(stdout, "testing\n"); 
			// case ':': fprintf(stdout, "EMOTIONAL DAMAGE\n"); 
			// default: fprintf(stdout, "fart\n");
		// }
	}
}