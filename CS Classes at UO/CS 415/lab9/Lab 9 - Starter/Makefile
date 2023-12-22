CFLAGS=-W -Wall
LIBRARIES=-lpthread
PROGRAMS=lab9 lab9-variable

all: $(PROGRAMS)

lab9: lab9.o
	gcc -o $@ $^ $(LIBRARIES)

lab9-variable: lab9-variable.o
	gcc -o $@ $^ $(LIBRARIES)

lab9.o: lab9.c
lab9-variable.o: lab9-variable.c

clean:
	rm -f *.o $(PROGRAMS)
