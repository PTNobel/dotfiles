CC=gcc
CFLAGS=-Wall
SOURCES=main.c
EXECUTABLE=music_wrapper

all:
	$(CC) $(CFLAGS) -o $(EXECUTABLE) $(SOURCES)
	strip $(EXECUTABLE)

debug:
	$(CC) $(CFLAGS) -o $(EXECUTABLE) $(SOURCES)

test:
	true

install:
	mkdir -p $(DESTDIR)/usr/local/bin/
	install -m 4755 $(EXECUTABLE) $(DESTDIR)/usr/local/bin/restricted/

clean:
	rm $(EXECUTABLE)
