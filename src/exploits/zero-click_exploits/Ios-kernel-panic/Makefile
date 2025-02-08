CC = gcc
CFLAGS = -Wall -Wextra -Werror

all: poc

poc: CVE-2021-1965-poc.o cli.o
	$(CC) $(CFLAGS) -o poc CVE-2021-1965-poc.o cli.o -lpcap

CVE-2021-1965-poc.o: CVE-2021-1965-poc.c logging.h
	$(CC) $(CFLAGS) -c CVE-2021-1965-poc.c

cli.o: cli.c
	$(CC) $(CFLAGS) -c cli.c

logging.o: logging.h
	$(CC) $(CFLAGS) -c logging.h

clean:
	rm -f poc CVE-2021-1965-poc.o cli.o logging.o
