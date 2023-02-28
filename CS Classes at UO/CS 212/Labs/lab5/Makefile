CLAGS=-g -W -Wall -I/usr/local/include
LDFLAGS=-L/usr/local/lib
OBJECTS=lab5.o
LIBRARIES=-lADTs -lm

all: lab5

lab5: $(OBJECTS)
	gcc $(LDFLAGS) -o $@ $^ $(LIBRARIES)

lab5.o: lab5.c

clean:
	rm -f lab5 $(OBJECTS)
