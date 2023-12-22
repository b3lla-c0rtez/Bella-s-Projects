#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <stdbool.h>
#define UNUSED __attribute__((unused))

typedef struct ticket {
	struct ticket *next;
	int value;
} Ticket;

typedef struct args {
	int id;
	bool ifBlocking;
} Args;

#define NTICKETS 10
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
Ticket tickets[NTICKETS];
Ticket *freeList = NULL;

volatile bool shutdown = false;

void initializeFreeList(void) {
	int i;

	for (i=0; i<NTICKETS; i++) {
		tickets[i].value = i;
		tickets[i].next = freeList;
		freeList = tickets + i;
	}
}

Ticket *getTicket(void) {
	Ticket *answer;
	pthread_mutex_lock(&lock);
	answer = freeList;
	if (answer != NULL) {
		freeList = answer->next;
	}
	pthread_mutex_unlock(&lock);
	return answer;
}

void putTicket(Ticket *ticket) {
	pthread_mutex_lock(&lock);
	ticket->next = freeList;
	freeList = ticket;
	pthread_mutex_unlock(&lock);
}

void *th_fxn(void *args) {
	Args *arg = (Args *)args;
	while (!shutdown) {
		long delay = 100000 + 20000 * (random()%50);
		Ticket *ticket = getTicket();
		if (ticket == NULL) {
			fprintf(stderr, "%d: No free tickets\n", arg->id);
		} else {
			fprintf(stderr, "%d: Obtained ticket %d", arg->id, ticket->value);
		}
		usleep(delay);
		if (ticket != NULL) {
			fprintf(stderr, "%d: Returned ticket %d\n", arg->id, ticket->value);
			putTicket(ticket);
		}
	}
	return NULL;
}

void onint(UNUSED int sig) {
	shutdown = true;
}

int main(int argc, char *argv[]) {
	int i, nthreads = 0;
	pthread_t threads[50];
	Args myargs[50];

	initializeFreeList();
	signal(SIGINT, onint);

	for (i=0; i<nthreads; i++) {
		myargs[i].id;
		pthread_create(threads+i, NULL, th_fxn, (void *)(myargs+i));
	}

	for (i = 0; i<nthreads; i++) {
		pthread_join(threads[i], NULL);
	}

	return EXIT_SUCCESS;
}