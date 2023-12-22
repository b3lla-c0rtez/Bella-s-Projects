#include "BXP/bxp.h"
#include <assert.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>
#include <pthread.h>
#define UNUSED __attribute__((unused))

int main(UNUSED int argc, UNUSED char *argv[]) {
	char test_string[] = "hello|this|is|a|test";
	char* test_array = strtok(test_string, " | ");
	int count = 0;

	if (strcmp(test_array, "hello") == 0) {
		printf("they're equal\n");
	} 
	/*if (strcmp(test_array, "this") == 0) {
		printf("this worked\n");
	} else {
		printf("nope, don't want to do this\n");
	}
	*/
	//OneShot|<clid>|<secs>|<usecs>|<host>|<service>|<port>
	//Repeat|<clid>|<secs>|<usecs>|<msecs>|<repeats>|<host>|<service>|<port>
	//Cancel|<svid>

	while (test_array != NULL) {
		printf("%s\n", test_array);
		test_array = strtok(NULL, " | "); 
		count++;
		//printf("count: %d\n", count);
	}


	printf("count: %d\n", count);
}
