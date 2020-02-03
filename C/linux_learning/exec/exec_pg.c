#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int exec_num = 56;

int main(int argc, char* argv[]) {
    printf("Exec_pg:\n");
    printf("\tMy pid is %d\n",(int) getpid());
    printf("\tArguments are");

    for(int i=0; i<argc; i++) {
        printf(" %s",argv[i]);
    }
    printf("\n");
    printf("\texec_num = %d\n",exec_num);
    return 0;
}
