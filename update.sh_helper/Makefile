CC=gcc
CFLAGS=-Wall  
SOURCES=main.c
EXECUTABLE=update_tools_helper

all:
	$(CC) $(CFLAGS) -o $(EXECUTABLE) $(SOURCES)
	strip $(EXECUTABLE)

install:
	install -m 4755 $(EXECUTABLE) /usr/local/bin/

clean:
	rm $(EXECUTABLE)
