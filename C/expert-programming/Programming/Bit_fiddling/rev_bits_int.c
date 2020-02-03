/*
 * How to reverse the bits in an interger?
 */
#include<stdio.h>
#include<stdlib.h>

int main(int argc, char *argv[]) {
        int n, temp = 0;

        printf("\nEnter the digit to be reversed: ");
        scanf("%d",&n);

        if(n<0)
                n = -n;

        while(n!=0) {
                temp = temp<<1;

                if(n&0x1)
                        temp = temp | 0x1;

                n = n>>1;
        }
        printf("\nreversed digit : %d",temp);

return 0;
}
