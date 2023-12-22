#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>	
#include <unistd.h>	
#define UNUSED __attribute__((unused))

long turn;
long nThreads;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;

void *func(void *args) {
    long myid = (long)args;
    for (;;) {
        pthread_mutex_lock(&lock);
        while (turn != myid) {
            pthread_cond_wait(&cond, &lock);
        }
        printf("performing task %ld\n", myid);
        usleep(100000L);
        turn = (turn+2) % nThreads;
        pthread_cond_broadcast(&cond);
        pthread_mutex_unlock(&lock);
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t t[25];
    long i;
    turn = 0L;
    nThreads = 20L;
    for (i=0L; i<nThreads; i++) {
       pthread_create(t+i, NULL, func, (void *)i);
    }
    for (i=0L; i<nThreads; i++) {
        pthread_join(t[i], NULL);
    }
    return EXIT_SUCCESS;
}
