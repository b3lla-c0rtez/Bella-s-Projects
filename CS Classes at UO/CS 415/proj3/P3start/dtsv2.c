#include "BXP/bxp.h"
#include <assert.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>
#include <pthread.h>
#define UNUSED __attribute__((unused))

/* 
Isabella Cortez, icortez6, CIS 415 Project 3
This is my own work, except that I received help from Andrew Teske 
He sent a toyfile that used string tokenize, and I was able to play
with the toyfile in order for it to print out the first word in the 
string that was used. I asked soem clarifying questions when it came
to count, and having to copy the query. I also found out I had to use
else if instead of if for the three cases.
*/

BXPEndpoint ep; 
BXPService svc; 
pthread_t request;

char query[10000], response[10001];
unsigned qlen, rlen;

void *req() {
	while((qlen = bxp_query(svc, &ep, query, 10000)) > 0) {
		char query_copy[qlen];
		strcpy(query_copy, query);
		char* q_array = strtok(query_copy, " | ");
		int count = 0;

		if (strcmp(q_array, "OneShot") == 0) {
			while (q_array != NULL) {
				q_array = strtok(NULL, " | "); 
				count+=1;
			}
			if (count == 7) {
				sprintf(response, "1%s", query);
			} else {
				//fprintf(stderr, "failed\n");
				sprintf(response, "0%s", query);
			}
		
		}
		
		else if (strcmp(q_array, "Repeat") == 0) {
			while (q_array != NULL) {
				q_array = strtok(NULL, " | "); 
				count+=1;
			}
			if (count == 9) {
				sprintf(response, "1%s", query);
			} else {
				sprintf(response, "0%s", query);
			}
		}

		else if (strcmp(q_array, "Cancel") == 0) {
			while (q_array != NULL) {
				q_array = strtok(NULL, " | "); 
				count+=1;
			}
			if (count == 2) {
				sprintf(response, "1%s", query);
			} else {
				sprintf(response, "0%s", query);
			}
		}
		
		rlen = strlen(response)+1;
		assert(bxp_response(svc, &ep, response, rlen));
	}
	return NULL;
}

int main(UNUSED int argc, UNUSED char *argv[]) {
	assert(bxp_init(19999, 1));
	assert((svc= bxp_offer("DTS")));
	pthread_create(&request, NULL, req, NULL);
	while (1) {

	}
	//return 0;
}