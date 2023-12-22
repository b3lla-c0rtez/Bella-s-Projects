CFLAGS=-W -Wall -pedantic -g
LDFLAGS=-g
OBJECTS=testharness.o packetdriver.o
LIBRARIES=./libTH.a
PROGRAMS= mydemo

all: $(PROGRAMS)

mydemo: $(OBJECTS)
	gcc -o $@ $(LDFLAGS) $^ $(LIBRARIES) -lpthread

clean:
	rm -f packetdriver.o mydemo

packetdriver.o: packetdriver.c
