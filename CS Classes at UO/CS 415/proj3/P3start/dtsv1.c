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
This is my own work, except that I received help from Andrew Teske to make 
sure I have the right part of the lab code in the void *req function
*/

BXPEndpoint ep; 
BXPService svc; 
pthread_t request;

char query[10000], response[10001];
unsigned qlen, rlen;

void *req() {
	while((qlen = bxp_query(svc, &ep, query, 10000)) > 0) {
		//printf("%d\n", qlen);
		sprintf(response, "1%s", query);
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