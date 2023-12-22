#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>	
#include <unistd.h>	
#define UNUSED __attribute__((unused))

long turn; 

pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;

void *func0(UNUSED void *args) {
    for (;;) {
        pthread_mutex_lock(&lock);
        while(turn != 0) {
            pthread_cond_wait(&cond, &lock);
        }
        printf("performing task 0\n");
        usleep(200000L);
        turn = 1;
        pthread_cond_signal(&cond);
        pthread_mutex_unlock(&lock);
    }
    return NULL;
}

void *func1(UNUSED void *args) {
    for (;;) {
        pthread_mutex_lock(&lock);
        while(turn != 1) {
            pthread_cond_wait(&cond, &lock);
        }
        printf("performing task 1\n");
        usleep(200000L);
        turn = 0;
        pthread_cond_signal(&cond);
        pthread_mutex_unlock(&lock);
    }
    return NULL;
}

int main(UNUSED int argc, UNUSED char *argv[]) {
    pthread_t t0, t1;
    turn = 0;
    pthread_create(&t0, NULL, func0, NULL);
    pthread_create(&t1, NULL, func1, NULL);
    pthread_join(t0, NULL);
    pthread_join(t1, NULL);
    return EXIT_SUCCESS;
}
