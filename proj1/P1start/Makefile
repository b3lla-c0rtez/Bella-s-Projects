CFLAGS=-W -Wall
# OBJECTS=uspsv1.o uspsv2.o uspsv3.o uspsv4.o
PROGRAMS=uspsv1 # uspsv2 uspsv3 uspsv4

all: $(PROGRAMS)

uspsv1: $(OBJECTS)
	gcc -g -o $@ $^
	# gcc -o uspsv1 uspsv1.o $(OBJECTS)

# uspsv2: $(OBJECTS)
#	gcc -o uspsv2 uspsv2.o $(OBJECTS)

# uspsv3: $(OBJECTS)
#	gcc -o uspsv3 uspsv3.o $(OBJECTS)

# uspsv4: $(OBJECTS)
#	gcc -o uspsv4 uspsv4.o $(OBJECTS)

uspsv1.o: uspsv1.c

# uspsv2.o: uspsv2.c

# uspsv3.o: uspsv3.c

# uspsv4.o: uspsv4.c

clean:
	rm -f $(PROGRAMS) *.o  # uspsv1.o uspsv2.o uspsv3.o uspsv4.o $(OBJECTS) $(PROGRAMS)