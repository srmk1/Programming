#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char *argv[]) {
        int n=0, q=0;

        scanf("%d",&n);
        //printf("%d\n",n);
        char **str_arr = (char **) malloc(n*sizeof(char *));

        for(int i=0; i<n; i++) {
                str_arr[i] = (char *) malloc(sizeof(char)*20);
                scanf("%s",str_arr[i]);
                //printf("%s\n",str_arr[i]);
        }

        scanf("%d",&q);
        //printf("%d\n",q);
        char *temp = (char *) malloc(sizeof(char)*20);
        int result[q];

        for(int i=0; i<q; i++) {

                scanf("%s",temp);
                //printf("%s\n",temp);

                result[i]=0;
                for(int j=0; j<n; j++)
                        if(strcmp(temp, str_arr[j])==0)
                                result[i]++;
                temp[0]='\0';
        }


        for(int i=0; i<q; i++) {
                printf("%d\n",result[i]);
        }

        free(str_arr);
        free(temp);

return 0;
}
