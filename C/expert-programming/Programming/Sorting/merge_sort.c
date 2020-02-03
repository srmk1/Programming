/* 
 * MergeSort(arr[], l,  r)
 * If r > l
 *    1. Find the middle point to divide the array into two halves:  
 *            middle m = (l+r)/2
 *    2. Call mergeSort for first half:   
 *            Call mergeSort(arr, l, m)
 *    3. Call mergeSort for second half:
 *           Call mergeSort(arr, m+1, r)
 *    4. Merge the two halves sorted in step 2 and 3:
 *            Call merge(arr, l, m, r)
 */
 
 #include<stdio.h>
#include<stdlib.h>

void merge(int arr[], int l, int m, int r) {
        int n1 = m-l+1;
        int n2 = r-m;
        int i, j, k;
        int left[n1], right[n2];

        for(i=0;i<n1;i++)
                left[i] = arr[l+i];
        for(j=0;j<n2;j++)
                right[j] = arr[m+j+1];

        i=0; j=0; k=l;

        while(i<n1 && j<n2)
                if(left[i] <= right[j])
                        arr[k++] = left[i++];
                else
                        arr[k++] = right[j++];

        while(i<n1)
                arr[k++] = left[i++];

        while(j<n2)
                arr[k++] = right[j++];

return;
}

void merge_sort(int arr[], int l, int r) {
        if(l<r) {
                int mid = (l+r)/2;
                merge_sort(arr, l, mid);
                merge_sort(arr, mid+1, r);
                merge(arr,l,mid,r);
        }
return;
}

int main(int argc, char *argv[]) {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr)/sizeof(arr[0]);

    for(int i=0;i<arr_size;i++)
        printf("%d\t",arr[i]);
        printf("\n");

    merge_sort(arr, 0, arr_size-1);

    printf("\nSorted array is \n");
    for(int i=0;i<arr_size;i++)
        printf("%d\t",arr[i]);

return 0;
}

             
