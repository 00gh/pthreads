CC=gcc
CFLAGS=-c -Wall
LDFLAGS=-pthread

all: mutex

mutex: main.o
	$(CC) main.o -o mutex $(LDFLAGS)

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

clean:
	rm *.o mutex
