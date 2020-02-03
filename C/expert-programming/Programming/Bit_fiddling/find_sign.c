/*
 * Detect if two Integers have opposite Signs (Bit Manipulation)
 */
#include<stdio.h>
#include<stdlib.h>

int find_sign(int i, int j) {

        /*
         * Below logic works.
         * But it involves branching.
         * We can avoid branching using bit manipultaion
        if(i>0 && j<0) {
                return 1;
        } else if(i<0 && j>0) {
                return 1;
        } else {
                return 0;
        }
         */

return ((i ^ j) < 0);
}

int main(int argc, char *argv[]) {
        int i = -1, j = 1;

        printf("Enter the digits to be compared:\n");
        scanf("%d\n%d",&i,&j);
        printf("Are these integers opposite sign: %d\n", find_sign(i,j));

return 0;
}
