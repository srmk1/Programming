#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/*
* i is globally declared
* It is being used by both child and parent
* Since both child and parent complete 5 loop count
* Both child and parent has a copy of i
* So, Both child and parent has its own Data segment 
*/
int i = 0;

void doSomeWork(char *str) {
    const int NUM_TIMES = 5;
    for (; i < NUM_TIMES; i++) {
            srand((int) getpid());
            sleep(rand() % 4);
            printf("Done pass %d under %s\n",i,str);
    }
}

int main(void) {
    int my_pid = (int) getpid();

    printf("My pid: %d\n",my_pid);
    /*
    * - Fork returns twices, once in parent and once in child
    *   - In child context
    *       - return value of fork is 0
    *       - So all the code of child is under ret value == 0
    *   - In parent context
    *       - return value of fork is pid of the parent 
    * - exit() terminates the process
    * - wait() in parents waits for state change of child
    */
    my_pid = fork();
    printf("Fork returned %d\n",my_pid);

    if (my_pid < 0) {
        perror("Fork failed\n");
    }

    if(my_pid == 0) {
        printf("I am child, my pid is %d\n",(int)getpid());
        /* 
        *  When just fork() is used
        *  - Text section is shared between parent and child
        *  - Verify by calling doSomeWork under both parent and child
        */
        doSomeWork("Child");
        printf("Child exiting\n");
        /*
        * exit has a return code
        * - 0 means success
        * - We can return any value
        */
        //exit(0);
        sleep(10);
        exit(42);

    }

    //We must be the parent
    printf("I am parent, my pid is %d\n",(int)getpid());
    printf("I am parent, waiting for child\n");
    doSomeWork("Parent");

    int ret_val = fork();

    if (ret_val == 0) {
        printf("I am the second child pid: %d\n",(int) getpid());
        exit(56);
    }

    /*
    * wait returns:
    * - pid of child on successful termination of child
    * - -1 on error of the child
    * Return status of the child can be captured in wait call
    *
    * If parent does not wait() on child:
    * - Then after child finishes its execution or calls exit()
    * - Kernel wont clean up the memory of the child process
    * - Such process is called as "Zombie process"
    * - ps -a such process will have <defunct> at the end of line
    */
    int status = 0;
    int childPid = wait(&status);
    printf("Parent knows that child %d finished",childPid);
    printf(" with status %d\n",status);
    /*
    * Status returns lot of things
    * - We can use Macro WEXITSTATUS to mask only return value
    */
    int childRetStatus = WEXITSTATUS(status); 
    printf("\tReturn value is %d\n",childRetStatus);
    sleep(5);
    return 0;
}
