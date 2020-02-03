/*
 * Repeatedly select the minimum element in the array and 
 * swap it with beginning element in order
 */
#include<stdio.h>
#include<stdlib.h>

void selection_sort(int a[], int n) {
        int i=0, j=0, min_idx=0, temp=0;

        for(i=0;i<n;i++) {
                min_idx = i;
                for(j=i+1;j<n;j++)
                        if(a[min_idx] > a[j])
                                min_idx = j;

                temp=a[min_idx];
                a[min_idx]=a[i];
                a[i]=temp;
        }
}

int main(int argc, char *argv[]) {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr)/sizeof(arr[0]);
    selection_sort(arr, n);
    printf("Sorted array: \n");
    for(int i=0; i<n; i++)
        printf("%d\t",arr[i]);

return 0;
}
