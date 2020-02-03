#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char *argv[]) {
        int n=0, q=0, idx=0, temp_seq=0;
        long x=0, y=0, lastans=0;


        scanf("%d %d",&n,&q);
        long **seq = (long **) malloc(n*sizeof(long*));;
        int *size = (int *) malloc(n*sizeof(int));

        for(int i=0; i<n; i++) {
                size[i] = 0;
                seq[i] = NULL;
        }

        for(int i=0; i<q; i++) {
                scanf("%d %ld %ld",&idx,&x,&y);

                if(idx == 1) {
                        temp_seq = (x^lastans)%n;
                        size[temp_seq]++;
                        seq[temp_seq] = (long *)realloc(seq[temp_seq],size[temp_seq]);
                        seq[temp_seq][size[temp_seq]-1] = y;
                        printf("Appending temp_seq=%d,idx=%d,y=%ld\n",temp_seq,size[temp_seq],y);
                }

                if(idx == 2) {
                    temp_seq = (x^lastans)%n;
                    lastans = seq[temp_seq][y%size[temp_seq]];
                    printf("%ld\n",lastans);
                }
        }

return 0;
}
