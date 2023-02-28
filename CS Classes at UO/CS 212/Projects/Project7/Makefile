CFLAGS=-g -W -I/usr/local/include
LDFLAGS=-L/usr/local/lib
LIBRARIES=-lADTs

all: exerciseQueue exerciseQueueADT

exerciseQueue: exerciseQueue.o
	gcc -o $@ $^ $(LIBRARIES)

exerciseQueueADT: exerciseQueue.o llistqueue.o
	gcc $(LDFLAGS) -o $@ $^ $(LIBRARIES)

exerciseQueue.o: exerciseQueue.c

llistqueue.o: llistqueue.c

clean:
	rm -f *.o exerciseQueue exerciseQueueADT
