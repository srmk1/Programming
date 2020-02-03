# Makefile for building programs
# Add more files under TARGETS to compile

TARGETS=fork fork_mchild fork_printf exec_pg exec_demo self_exec
CC_C= gcc
C_FLAGS= -Wall -g -std=c99 -Werror

all: clean $(TARGETS)

$(TARGETS):
	$(CC_C) $(C_FLAGS) $@.c -o $@

clean:
	rm -f $(TARGETS)
