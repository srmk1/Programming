/*
 * If you know that a huge array of elements contains many reptitive elements
 * And we know it be max of say n bits.
 * Maximum value present in array can 2pown
 * - Create a count array of 2pown
 * - Parse array and increment count[arr[i]]++
 * - for each element in count array: count[i] += count[i-1]
 * - Parse array again to populare output array: output[count[arr[i]]-1] = arr[i] and decrement count
 */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void count_sort(int num[], int bits_len, int len) {
        int *count = (int *) malloc((bits_len+1)*sizeof(int));
        int output[len+1];

        memset(count, 0, (bits_len+1)*sizeof(int));

        for(int i=0; i<len; i++)
                count[num[i]]++;

        /*gives the index of the a[i] in output array*/
        for(int i=1; i<=bits_len; i++)
                count[i] += count[i-1];

        for(int i=0; i<len; i++) {
                output[count[num[i]]-1]=num[i];
                count[num[i]]--;
        }

        for(int i=0; i<len; i++)
                printf("%d\t",output[i]);
return;
}

int main(int argc, char *argv[]) {
        int a[] = {1, 4, 1, 2, 7, 5, 2};
        count_sort(a,7,7);

return 0;
}
