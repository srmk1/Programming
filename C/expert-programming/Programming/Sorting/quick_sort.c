#include<stdio.h>
#include<stdlib.h>

int partition(int a[], int l, int r) {
        int pivot = a[r];
        int i = l-1, temp = 0;

        for(int j=l; j<r; j++)
                if(a[j] < pivot) {
                        i++;
                        temp = a[i];
                        a[i] = a[j];
                        a[j] = temp;
                }

                        temp = a[i+1];
                        a[i+1] = a[r];
                        a[r] = temp;
return i+1;
}
void quick_sort(int a[], int l, int r) {
        if (l < r) {
                int p=partition(a, l, r);
                quick_sort(a,l,p-1);
                quick_sort(a,p+1,r);
        }
return;
}

int main(int argc,char *argv[]) {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr)/sizeof(arr[0]);
    quick_sort(arr, 0, n-1);
    printf("Sorted array: \n");
    for(int i=0;i<n;i++)
        printf("%d\t",arr[i]);
    printf("\n");
return 0;
}
