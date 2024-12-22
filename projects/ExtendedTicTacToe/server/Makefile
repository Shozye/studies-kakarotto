SOURCES = $(wildcard *.c)
BINARY = $(patsubst %.c, %, $(SOURCES))

FLAGS = -W -pedantic -std=c17 -O3
.PHONY = all clean

all: $(BINARY)

$(BINARY): %: %.c
	$(CC) $(FLAGS) $^ -o $@
	strip $@

clean:
	rm -f $(BINARY)

