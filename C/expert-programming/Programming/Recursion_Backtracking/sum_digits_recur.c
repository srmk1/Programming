#include<stdio.h>
#include<stdlib.h>

int sum_digits(int n) {
        int sum = 0;

        if (n == 0) {
                return 0;
        } else {
                sum += (n%10) + sum_digits(n/10);
        }
return sum;
}

int main(int argc, char *argv[]) {
        int n = 1234;

        printf("Sum of digits of %d is %d\n",n,sum_digits(n));

return 0;
}
