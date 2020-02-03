#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>

int main() {
    printf("Why am i printed twice");

    int pid = fork();
    if (pid == 0) {
        printf("\n");
        exit(0);
    }

    printf("\n");

    return 0;
}
