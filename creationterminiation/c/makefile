# Most systems with clang sym link to gcc so to be let's define gcc
CC=gcc
CFLAGS=-c -Wall
LDFLAGS=-pthread

all: hello

hello: main.o 
	$(CC)  main.o -o hello

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

clean: 
	rm *.o hello	
