#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/wait.h>

void forker(int n) {
    int pid = 0;

    if (n == 0) {
        return;
    }
    n--;
    pid = fork();

    if (pid == 0) {
        //child process
        printf("Child process %d pid %d\n",n,(int) getpid());
        sleep(5);
        exit(0);
    }

    /* 
     * To create 10 child process
     * easy way is to use recursive process and calling
     * recursive function in parent context
     */
    forker(n);
    int status;
    int wpid = wait(&status);
    printf("Parent knows that child %d exited\n",wpid);
    return;
}

int main(int argc, char *argv[]) {
    forker(10);
    return 0;
}
