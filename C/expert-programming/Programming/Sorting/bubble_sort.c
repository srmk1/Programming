/*
 * Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
 */
#include<stdio.h>
#include<stdlib.h>

void bubble_sort(int a[], int n) {
        int i=0, j=0, temp=0;
        int swapped = 0;
        for(i=0; i<n; i++) {
                swapped = 0;
                for (j=0;j<n-i-1;j++)
                        if(a[j] < a[j+1]) {
                                temp = a[j];
                                a[j]=a[j+1];
                                a[j+1]=temp;
                                swapped = 1;
                        }
                if(!swapped)
                        break;
        }
}
int main(int argc, char *argv[]) {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    bubble_sort(arr, n);
    printf("Sorted array: \n");
    for(int i=0; i<n; i++)
        printf("%d\t",arr[i]);
return 0;
}
