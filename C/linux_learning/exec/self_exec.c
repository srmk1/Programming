#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
int self_exec_gbl = 33;

int main(int argc, char *argv[]) {
    char *args[] = {"./self_exec","Hello", "World",NULL};

    printf("self_exec: My pid is %d\n",(int) getpid());
    printf("self_exec_gbl=%d\n",self_exec_gbl);
    self_exec_gbl -= 30;
    /*
     * Replacing self program using exec
     * results in a infinite loop of execution
     */
    execvp(args[0],args);
    return 0;
}
