/*
 * Check Saurabh school:
 * https://www.youtube.com/watch?v=ScF985Y4DJc&index=5&list=PLTZbNwgO5ebpTHdT7ylOTO2dX00QoDh4q
 * https://www.youtube.com/watch?v=YJa3GpNUrNs&index=4&list=PLTZbNwgO5ebpTHdT7ylOTO2dX00QoDh4q
 */
#include<stdio.h>
#include<stdlib.h>

void max_heapify(int a[], int pos, int len) {
        int largest = pos, temp;
        int left = (2*pos)+1;
        int right = (2*pos)+2;

        if(left < len && a[left] > a[largest])
                largest = left;


        if(right < len && a[right] > a[largest])
                largest = right;

        printf("\npos=%d\tlargest=%d\n",pos,largest);
        if(largest != pos) {
                temp = a[largest];
                a[largest] = a[pos];
                a[pos] = temp;

                max_heapify(a,largest,len);
        }
}

void heap_sort(int a[], int n) {
        for(int i = n/2-1;i>=0; i--)
                max_heapify(a,i,n);

        for(int i=0;i<n;i++)
                printf("%d\t",a[i]);
}
int main(int argc, char *argv[]) {
        int arr[] = {12, 11, 13, 5, 6, 7};
        int len = sizeof(arr)/sizeof(int);
                 heap_sort(arr, len);

return 0;
}
