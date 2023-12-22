CFLAGS=-W -Wall

prodcons: prodcons.o
	gcc -o $@ $^ libTH.a -lpthread

prodcons.o: prodcons.c

clean:
	rm -f prodcons prodcons.o
