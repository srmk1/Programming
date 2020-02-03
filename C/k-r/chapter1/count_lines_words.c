#include<stdio.h>

#define OUT 1
#define IN 2

int main(int argc,char *argv[]) {
	int c, cl = 0, cw = 0, ct = 0, cc = 0;
	int state = OUT;

	while ( (c=getchar()) != EOF ) {
		cc++;
		if (c == '\n')
			cl++;

		if (c == '\t')
			ct++;

		if (c == ' ' || c == '\t' || c == '\n') {
			state = OUT;
		} else if (state == OUT) {
			state = IN;
			cw++;
		}
	}
	printf("Number of lines = %d\n",cl);
	printf("Number of words = %d\n",cw);
	printf("Number of tabs = %d\n",ct);
	printf("Number of character = %d\n",cc);

return 0;
}
