#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

int main(int argc, char *argv[]) {

    int ret_val = fork();

    /*
     * execute linux standard commands
     * using execvp
     */
    if(ret_val == 0) {
        char *args[] = {"ps", NULL};
        execvp("ps", args);
        printf("\n");
        exit(0);
    }

    return 0;
}
