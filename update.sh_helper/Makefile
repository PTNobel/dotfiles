CC=gcc
CFLAGS=-Wall  
SOURCES=main.c
EXECUTABLE=update_tools_helper

all:
	$(CC) $(CFLAGS) -o $(EXECUTABLE) $(SOURCES)
	strip $(EXECUTABLE)

debug:
	$(CC) $(CFLAGS) -o $(EXECUTABLE) $(SOURCES)

install:
	install -m 4755 $(EXECUTABLE) /usr/local/bin/

clean:
	rm $(EXECUTABLE)
