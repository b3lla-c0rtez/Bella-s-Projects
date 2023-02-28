#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#define UNUSED __attribute__((unused))

int main(UNUSED int argc, UNUSED char *argv[]){
	char buf[BUFSIZ];
	char last[BUFSIZ] = "";
	
	while(fgets(buf, BUFSIZ, stdin) != NULL)
		if(strcasecmp(buf, last) != 0) {
			printf(last);
			strcpy(last, buf);
		}
	printf(last);
}
