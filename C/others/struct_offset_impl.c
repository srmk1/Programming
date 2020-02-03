#include<stdio.h>
#include<stddef.h>

/*
 * The offsetof() macro is an ANSI-required macro that should be found in stddef.h. 
 * Simply put, the offsetof() macro returns the number of bytes of offset before a particular element of a struct or union.
 * 
 * Implementation:
 * // Keil 8051 compiler
 * #define offsetof(s,m) (size_t)&(((s *)0)->m)
 * (
 *   (int)(         // 4.
 *     &( (         // 3.
 *       (a*)(0)    // 1.
 *      )->b )      // 2.
 *   )
 * )
 *
 * #define offsetof(type,member) ((size_t)(&((type *)0)->member))
 *
 * Working from the inside out, this is ...
 * 
 * Casting the value zero to the struct pointer type a*
 * Getting the struct field b of this (illegally placed) struct object
 * Getting the address of this b field
 * Casting the address to an int
 * Conceptually this is placing a struct object at memory address zero and 
 * then finding out at what the address of a particular field is. 
 * This could allow you to figure out the offsets in memory of each field in a struct so you could 
 * write your own serializers and deserializers to convert structs to and from byte arrays.
 * 
 * Of course if you would actually dereference a zero pointer your program would crash, 
 * but actually everything happens in the compiler and no actual zero pointer is dereferenced at runtime.
 * 
 * In most of the original systems that C ran on the size of an int was 32 bits and was the same as a pointer, 
 * so this actually worked.
 */

struct offset_struct {
	int a;
	float b[10];
	char c;
};

// It also works for nested structs
struct offset_struct_nested {
	int d;
	char e[10];
	struct offset_struct f;
};

int main(int argc, char* argv[]) {

	printf("Offset of 'a' is %lu\n",offsetof(struct offset_struct, a));
	printf("Offset of 'b' is %lu\n",offsetof(struct offset_struct, b));
	printf("Offset of 'c' is %lu\n",offsetof(struct offset_struct, c));

	// It also works for nested structs
	printf("Offset of 'd' is %lu\n",offsetof(struct offset_struct_nested, d));
	printf("Offset of 'e' is %lu\n",offsetof(struct offset_struct_nested, e));
	printf("Offset of 'f' is %lu\n",offsetof(struct offset_struct_nested, f));
	printf("Offset of 'f->a' is %lu\n",offsetof(struct offset_struct_nested, f.a));
	printf("Offset of 'f->b' is %lu\n",offsetof(struct offset_struct_nested, f.b));
	printf("Offset of 'f->c' is %lu\n",offsetof(struct offset_struct_nested, f.c));
return 0;
}
