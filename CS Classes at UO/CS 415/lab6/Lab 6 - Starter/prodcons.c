#include "BoundedBuffer.h"
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdbool.h>
#define UNUSED __attribute__((unused))

long delay = 10 * 1000L;
bool isBlocking = false;
BoundedBuffer *bb = NULL;
bool prodDone = false;

void *producer(UNUSED void *args) {
    char buf[BUFSIZ];
    while (fgets(buf, sizeof buf, stdin) != NULL) {
        char *s = stdrup(buf);
        usleep(delay);
        if (isBlocking) {
            bb->blockingWrite(bb, (void *)s);
        } else if (!bb->nonblockingWrite(bb, (void *)s)) {
            free(s);
        }
    }
    prodDone = true;
    return NULL;
}

void *consumer(UNUSED void *args) {
    char *s;
    while (! prodDone) {
        usleep(2 * delay);
        bb->blockingRead(bb, (void **)&s);
        fputs(s, stdout);
        free(s);
    }
    while (bb->nonblockingRead(bb, (void **)&s)) {
        fputs(s, stdout);
        free(s);
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    int opt;
    int size = 10;
    pthread_t prod_id, cons_id;
    opterr=0;
    while ((opt = getopt(argc, argv, "bn:d:")) != -1) {
        switch(opt) {
            case 'b': isBlocking = true; break;
            case'n': size = atoi(optarg); break;
            case 'd': delay = 1000*atoi(optarg); break;
            default: fprintf(stderr, "illegal options"); return EXIT_FAILURE;
        }
    }
    bb = BoundedBuffer_create(size);
    pthread_create(&cons_id, NULL, consumer, NULL);
    pthread_create(&prod_id, NULL, producer, NULL);
    pthread_join(prod_id, NULL);
    pthread_join(cons_id, NULL);
    return EXIT_SUCCESS;
}
