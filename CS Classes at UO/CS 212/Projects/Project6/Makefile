CFLAGS=-g -W -Wall -I/usr/local/include
LDFLAGS=L/usr/local/lib
LIBRARIES=-lADTs
PROGRAMS= exerciseStack balanceCheck

all: $(PROGRAMS)

exerciseStack: exerciseStack.o
	gcc -o $@ $^ $(LIBRARIES)

exerciseStack.o: exerciseStack.c

balanceCheck: balanceCheck.o
	gcc -o $@ $^ $(LIBRARIES)

balanceCheck.o: balanceCheck.c

clean:
	rm -f *.o $(PROGRAMS)

