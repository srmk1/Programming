include<stdio.h>
#include<stdlib.h>

void print_array(int a[], int n) {

        printf("%d\n",a[n]);

        if(n==0) {
                return;
        } else {
                print_array(a,n-1);
                printf("%d\n",a[n]);
        }

return;
}
int main(int argc, char *argv[]) {
        int arr[10] = { 1,2,3,4,5,6,7,8,9,10};

        print_array(arr,9);
return 0;
}
