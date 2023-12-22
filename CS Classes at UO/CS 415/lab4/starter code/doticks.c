#include <unistd.h>	/* defines _exit() */
#include <stdlib.h>	/* defines NULL, getenv() */
#include <time.h>	/* needed for struct timespec and nanosleep */
#include <sys/time.h>   /* needed for gettimeofday(), struct timeval */
                        /* and for setitimer(), struct itimerval */
#include <signal.h>     /* signal(), kill(), USR1, USR2, STOP, CONT */
#include <stdbool.h>	/* bool, true, false */
#include <stdio.h>

#define UNUSED __attribute__((unused))
#define QUANTUM 1000

int ticks = 0;
int tick = 250;

volatile bool shutdown = false;

static void onalarm(UNUSED int sig) {
    if (ticks>0) {
        printf("%d ticks\n", ticks--);
    } else {
        ticks = QUANTUM/tick;
        printf("Resetting tick count\n");
    }
}

static void onint(UNUSED) {
    printf("C signal received! \n");
    shutdown = true;
}

int main(int argc, char **argv) {
    struct itimerval it_val;
    struct timespec ms20 = {0, 20000000};
    if (argc==2) {
        tick = atoi(argv[1]);
    }
    signal(SIGINT, onit);
    signal(SIGALRM, onalrm)

    it_val.it_value.tv_sec = tick/1000;
    it_val.it_value.tv_usec = (tick*1000) % 1000000;
    it_val.it_interval = it_val.it_value;
    if (setitimer(ITIMER_REAL, &it_val, NULL) == -1) {
        fprintf(stderr, "error");
    }

    while (!shutdown) {
        nanosleep(&ms20, NULL);
    }

    return EXIT_SUCCESS;
}
