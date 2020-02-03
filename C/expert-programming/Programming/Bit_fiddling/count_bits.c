//Write a C program to count bits set in an integer
#include<stdio.h>
#include<stdlib.h>

int main(int argc, char *argv[]) {
        unsigned int n = 0, count = 0;
        unsigned long long ln = 0, lcount = 0;

        printf("\nEnter the digit: ");
        scanf("%x",&n);
        printf("\nEnter the long digit: ");
        scanf("%llx",&ln);
        
        printf("Number of bits = %d\n",__builtin_popcount(n));
        printf("Number of bits = %d\n",__builtin_popcountll(ln));

return 0;
}

/*
int main(int argc, char *argv[]) {
        int n, count = 0;

        printf("\nEnter the digit: ");
        scanf("%d",&n);

        while(n != 0) {
                if(n & 0x1)
                        count++;
                n = n>>1;
        }

        printf("Number of bits = %d\n",count);

return 0;
} */

/*
#include<stdio.h> 

int main() { 
  int num=10; 
  int ctr=0; 
  
  while(num) { 
      ctr++; 
      num = num & (num - 1); // This clears the least significant bit set. 
  }
  
printf("\n Number of bits set in [%d] = [%d]\n", num, ctr); 
return(0); 
} */
