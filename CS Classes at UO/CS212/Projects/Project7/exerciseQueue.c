#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "ADTs/queue.h"

#define UNUSED __attribute__((unused))

void printQueue(const Queue *q, FILE *fp){
	long i, N;
       	
	if(q->isEmpty(q)){
		fprintf(fp,"Empty\n");
		return;
	} else {
	
	const Iterator *it = q->itCreate(q);
	
	N = q->size(q);
	while(it->hasNext(it)) {
	for(i=0; i<N; i++) {
		long temp;
		it->next(it, (void **)&temp);
		if(i < N-1){
			fprintf(fp, "%ld ", temp);
		} else {
			fprintf(fp, "%ld\n", temp);
		}
	}
	}
	it->destroy(it);
	//fprintf(fp, "\n");
	}
}

int main(UNUSED int argc, UNUSED char *argv[]) {
	int exitStatus = EXIT_FAILURE;
	const Queue *q = Queue_create(doNothing);

	if(q == NULL) {
		printf("Unable to create queue, :C\n");
		return exitStatus;
	} 
	
	FILE *fp;
	fp = fopen(argv[1], "r");

	char buf[BUFSIZ];
	long value;

	fgets(buf, BUFSIZ, fp);
	sscanf(buf, "%ld",&value);

	for(int i = value; i > 0; i--){
		fgets(buf, BUFSIZ, fp);

		if ((strcmp(buf, "print\n")) == 0) {
			printQueue(q, stdout);
		}

		else if ((strcmp(buf, "dequeue\n")) == 0) {
			long d;
			if(! q->dequeue(q, ADT_ADDRESS(&d))) {
				printf("QueueError\n");
			} else {
				printf("%ld\n", d);
			}
		
		} else {
			long e;
			sscanf(buf+8, "%ld", &e);
			q->enqueue(q, ADT_VALUE(e));
		}
	}
	
	
	q->destroy(q);
	fclose(fp);
	exitStatus = EXIT_SUCCESS;
	return exitStatus;
}
