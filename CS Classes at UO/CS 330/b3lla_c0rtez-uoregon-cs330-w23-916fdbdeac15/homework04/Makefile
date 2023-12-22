sources = graph.c matrix.c load.c main.c
objects = $(addsuffix .o, $(basename $(sources)))
flags = -g -W -Wall -std=c11 -DDEBUG=0 -DTEST=0
target = bfs 

all: $(target)

$(target) : $(objects)
	gcc -o $(target) $(objects)

%.o : %.c
	gcc -c $(flags) $< -o $@
clean :
	rm $(target) $(objects)
