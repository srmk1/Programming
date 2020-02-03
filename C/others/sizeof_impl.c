#include <stdio.h>

typedef struct{
	char c;
	int i;
	float f;
	double d;
}s;

#define my_sizeof(type) (char *)(&type+1)-(char*)(&type)

int main(int argc, char* argv[]) {
	char c;

        short s2; 
        int i;
        long l;
        long int li; 
        long long ll; 

        unsigned short s21;
        unsigned int i1; 
        unsigned long l1; 
        unsigned long long ll1;

        float f;
        double d;
        long double ld; 
        //double double dd; //throws compilation error

        s s1; 

        printf("Sizeof char is %lu\n\n", my_sizeof(c));

        printf("Sizeof short is %lu\n", my_sizeof(s2));
        printf("Sizeof int is %lu\n", my_sizeof(i));
        printf("Sizeof long is %lu\n", my_sizeof(l));
        printf("Sizeof long int is %lu\n", my_sizeof(li));
        printf("Sizeof long long is %lu\n\n", my_sizeof(ll));

        printf("Sizeof unsigned short is %lu\n", my_sizeof(s21));
        printf("Sizeof unsigned int is %lu\n", my_sizeof(i1));
        printf("Sizeof unsigned long is %lu\n", my_sizeof(l1));
	printf("Sizeof unsigned long long is %lu\n\n", my_sizeof(ll1));

        printf("Sizeof float is %lu\n", my_sizeof(f));
        printf("Sizeof double is %lu\n", my_sizeof(d));
        //printf("Sizeof double double is %lu\n", my_sizeof(dd));
        printf("Sizeof long double is %lu\n\n", my_sizeof(ld));

        printf("Sizeof structure is %lu\n", my_sizeof(s1));
        getchar();

return 0;
}
