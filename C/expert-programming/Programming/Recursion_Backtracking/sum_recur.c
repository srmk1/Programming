#include<stdio.h>

int sum(int n) {
        int val = 0;

        if(n == 0) {
                return 0;
        } else {
                val += n + sum(n-1);
        }

return val;
}

int main(int argc, char *argv[]) {
        int n = 10;

        printf("\nSum of natural numbers till %d is %d",n, sum(n));

return 0;
}
