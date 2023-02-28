#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "stringlist.h"
#include "stringlist.c"

#define UNUSED __attribute__((unused))

int main (UNUSED int argc, UNUSED char *argv[]) {
	const StringList *sl;
	int i;
	char buf[BUFSIZ];
	char *index;

	if((sl = StringList_create(50L)) == NULL) {
		fprintf(stderr, "%s: error allocating on heap \n", argv[0]);
		return EXIT_FAILURE;
	}
	while(fgets(buf, sizeof(buf), stdin) != NULL) {
		bool apd = sl->append(sl, strdup(buf));
		if(apd == false){
			fprintf(stderr, "%s: error \n", buf);
			sl->destroy(sl);
			return EXIT_FAILURE;
		}
	}
	int N = sl->size(sl);	
	for(i = N - 1; i >= 0L; i--){
		sl->get(sl, i, &index);
		printf("%s", index);
	}

	sl->destroy(sl);
	return EXIT_SUCCESS;
}
