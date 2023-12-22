#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <stdbool.h>
#define NUMBER 129

int main(int argc, char *argv[]) {
	for (int i; i<argc; i++) {
		printf("%s\n", argv[i]);
	}
}