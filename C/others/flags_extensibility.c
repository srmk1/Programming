#include<stdio.h>
#include<unistd.h>

#define OLD_FUNC1 0x1
#define OLD_FUNC2 0x2
#define OLD_FUNC3 0x4

/*
* Flags argument in the api to ensure extensibility.
*
* Reference: https://kernel.org/doc/html/latest/process/adding-syscalls.html#designing-the-api-planning-for-extension
* A new system call forms part of the API of the kernel, and has to be supported indefinitely. 
* As such, it’s a very good idea to explicitly discuss the interface on the kernel mailing list, 
* and it’s important to plan for future extensions of the interface.
*
* For simpler system calls that only take a couple of arguments, 
* the preferred way to allow for future extensibility is to include a flags argument to the system call. 
* To make sure that userspace programs can safely use flags between kernel versions, 
* check whether the flags value holds any unknown flags, and reject the system call (with EINVAL) if it does:
* 	if (flags & ~(THING_FLAG1 | THING_FLAG2 | THING_FLAG3))
*		return -EINVAL;
* References:
* https://lwn.net/Articles/585415/
* https://lwn.net/Articles/588444/
* 
* In particular, a system call flags argument (or indeed any input structure argument that has a bit-flags field) 
* should always include a check of the following form in its implementation:
*	if (flags & ~(FL_XXX | FL_YYY))
*		return -EINVAL;
* Here, FL_XXX and FL_YYY form the hypothetical set of flags that the system call understands, 
* and the effect of this check is to deliver an error when the caller specifies any bit value other than one in the set. 
* Checks like this future-proof the API against the day when the system call understands additional flags. 
* Suppose that the system call adds a new flag, FL_ZZZ, and adjusts its check to:
*
* 	if (flags & ~(FL_XXX | FL_YYY | FL_ZZZ))
*		return -EINVAL;
*
*/
int old_api(unsigned long flags) {

    if(flags & ~(OLD_FUNC1 | OLD_FUNC2 | OLD_FUNC3)) {
        /*  Any flags apart from this not supported */
        return 0;
    }

    return 1;
}

int main(int argc, char *argv[]) {

    printf("Trying to access new functionality\n");

    if(old_api(0x8)) {
        printf("Hurray new functionality\n");
        return 0;
    }

    if(old_api(0x4)) {
        printf("Old functionality\n");
    }

    return 0;
}
