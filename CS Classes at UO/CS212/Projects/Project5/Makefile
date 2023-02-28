CFLAGS=-g -W -Wall -I/usr/local/include
LDFLAGS=-L/usr/local/lib
LIBRARIES=-lADTs
PROGRAM=reverse
OBJECTS=stringlist.o reverse.o
cc=gcc

all: $(PROGRAM)

reverse: reverse.o
	gcc -o $@ $^ $(LIBRARIES)

stringlist.o: stringlist.h stringlist.c

reverse.o: reverse.c stringlist.h

clean:
	rm -f *.o $(PROGRAM)
