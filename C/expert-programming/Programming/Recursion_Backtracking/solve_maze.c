/*
 * Move up, down, left, right and check if its safe.
 *
 * When declaring a function which takes 2 dimensional array as argument:
 *   - you need to index of second argument
 *   - OR you need to pass it as double pointer
 *   - Check http://stackoverflow.com/questions/10003270/gcc-array-type-has-incomplete-element-type
 *   - int solve_maze(int lmaze[][5], int x, int y, int n, int lsol[][5]) {
 *
 * Intializing two dimensional array notices the usage of {
 *    - int sol[5][5] = { {0},{0},{0},{0},{0} };
 */
 #include<stdio.h>
#include<stdlib.h>

int maze[5][5] = { {1, 1, 1, 0, 0},
                   {0, 0, 1, 1, 0},
                   {1, 0, 0, 1, 0},
                   {0, 1, 0, 1, 1},
                   {0, 0, 0, 0, 1} };

int is_safe(int lmaze1[][5], int x, int y, int n) {

        if ( (x>=0) && (x<n) && (y>=0) && (y<n)
                && (lmaze1[x][y] == 1) )
                return 1;
return 0;
}

int solve_maze(int lmaze[][5], int x, int y, int n, int lsol[][5]) {
        if(x==n-1 && y==n-1) {
                if(is_safe(lmaze,x,y,n)) {
                        lsol[x][y] = 1;
                        return 1;
                } else {
                        lsol[x][y] = 0;
                        return 0;
                }
        }
        if(is_safe(lmaze, x, y, n)) {
                lsol[x][y] = 1;
                if(solve_maze(lmaze,x+1, y, n, lsol)) return 1;
                if(solve_maze(lmaze,x, y+1, n, lsol)) return 1;
                if(solve_maze(lmaze,x-1, y, n, lsol)) return 1;
                if(solve_maze(lmaze,x, y-1, n, lsol)) return 1;
                lsol[x][y] = 0;
                return 0;
        }
return 0;
}

}
int main(int argc, char *argv[]) {
        int sol[5][5] = { {0},{0},{0},{0},{0} };
        if(solve_maze(maze, 0, 0, 5, sol)) {
                printf("solved: \n");
                for(int i=0; i<5; i++) {
                        for(int j=0; j<5; j++)
                                printf("%d\t",sol[i][j]);
                        printf("\n");
                }
        }
return 0;
}

