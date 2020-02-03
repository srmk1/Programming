#include<stdio.h>
#include<stdlib.h>

int binary_search(int a[], int key, int start, int n) {
        int mid = (start + n) / 2;

        if(start > n) {
                return 0;
        }

        if (a[mid] == key) {
                printf("Found the element\n");
                return 1;
        }
        else
        if(a[mid] < key)
                binary_search(a, key, mid+1, n);
        else
                binary_search(a, key, start, mid-1);


return 0;
}

int main(int argc, char *argv[]) {
        int a[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        int key;

        printf("\nEnter the key to be searched: ");
        scanf("%d",&key);

        binary_search(a, key, 0, 9);

return 0;
}
