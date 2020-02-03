#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>

int exec_num = 100;

int main(int argc, char *argv[]) {
    char *args[] = {"./exec_pg", "Hello", "Aditi", NULL};

    /*
    * When exec() api is called:
    * - First argument is path of executable(progam having main)
    * - Second argument - list of arguments
    * New executable will inherent all the address space of its
    * caller. Text section will be replaced by the new 
    * text from executable, data section will also be of new 
    * executable.
    * Exec() api never returns to its caller, so any code
    * after exec call will never be executed
    * after exec call will never be executed. Though the same
    * pid, address space..etc is continued to use
    *
    * exec has following variants:
    * - execv, execvp, execvpe
    * - execl, execlp, execlpe
    *
    * With L: comma separated arguments
    * With V: Vector as arguments i.e. array of strings
    * With P: Include search path for executable 
    *
    * If a process exec() itself, then it would continue
    * in infinite loop exec itself everytime
    */
    printf("Exec Demo program process id: %d\n",(int) getpid());
    printf("exec_num = %d\n",exec_num);
    execvp(args[0],args);

    printf("We will never get this printf\n");
    return 0;
}

