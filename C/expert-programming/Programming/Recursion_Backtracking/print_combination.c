/*
 * Basic idea behind combination of string is
 * Think of the combinations as bit encodings. E.g.
 * empty = 000 = 0
 * C = 001 = 1
 * B = 010 = 2
 * BC = 011 = 3
 * A = 100 = 4
 * AC = 101 = 5
 * AB = 110 = 6
 * ABC = 111 = 7
 * Algorithm:
      Given a string on length n:
        - Get the bit encodings of all values from 0 to 2(pow)n
        - For each bit encoding print the character corresponding to bits having 1
 */

#include<stdio.h>
#include<stdlib.h>

char b[5] = {'a', 'b', 'c', 'd', '\0'};

void print_com(int bit[], int n) {
        for(int i=0; i<n; i++) {
                if(bit[i] == 1)
                        printf("%c",b[i]);
        }
        printf("\n");
return;
}
void combination(int bit[], int pos, int n) {
        if(pos == n-1) {
                bit[pos] = 0;
                print_com(bit, n);
                bit[pos] = 1;
                print_com(bit, n);
                return;
        } else {
                bit[pos] = 0;
                combination(bit, pos+1, n);
                bit[pos] = 1;
                combination(bit, pos+1, n);
        }
return;
}

int main(int argc, char *argv[]) {
        int bit[10] = {0};
        combination(bit, 0, 4);
return 0;
}
 
