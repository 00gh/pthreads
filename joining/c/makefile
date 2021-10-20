# Most systems with clang sym link to gcc so to be let's define gcc
CC=gcc
CFLAGS=-c -Wall
LDFLAGS=-pthread -lm

all: joining

joining: main.o 
	$(CC)  main.o -o joining $(LDFLAGS)

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

clean: 
	rm *.o joining
