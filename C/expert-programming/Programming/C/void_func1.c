#include <stdio.h>
int main()
{
    static int i = 5;
    if (--i){
        printf("%d ", i);
        main(10);
    }
    printf("\n");
}

/* COMPILES AND EXECUTES
SRMK-M-H00U:linux srmk$ gcc void_func.c -o void_func
SRMK-M-H00U:linux srmk$ ./void_func 
4 3 2 1 
*/
