#include<stdio.h>

#define NOT_SPACE 'a' 
#define SPACE ' ' 

int main(int argc,char *argv[]) {
	int c, prev_char = NOT_SPACE;

	while ( (c=getchar()) != EOF ) {
		if ( c == ' ' && prev_char == ' ')
			;
		else
			putchar(c);

		prev_char = c;
	}
			
return 0;
}
