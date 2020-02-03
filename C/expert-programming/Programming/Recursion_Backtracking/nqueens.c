#include<stdio.h>
#include<stdlib.h>

/*
 * Give a nxn chess board
 * Place n queens in it such that they dont cross each other
 * Rules for queen to cut each other
 * - If its in same row
 * - If its in same column
 * - If its in diagonal
 *
 * Solution:
 * - Lets store the co-ordinates in an integer array
 *   where index to array represents row
 *   array[index] represents the column
 * - Start placing from each row
 *   Once you are able to place in a row move to next row
 * - place api checks for conditions given above
 *   We always never try to place them in same row, so its taken
 *   Checking if its in same column is simple
 *   Checking for diagonal:
 *     (difference of x co-ordinates) == (difference of y coordintes)
 */

int pos[8];     //index=row, pos[index]=column

int place(int row, int col) {

        for(int j = 1; j<row; j++) {
                if(pos[j] == col || (abs(j-row) == abs(pos[j]-col)))
                        return 0;
        }
return 1;
}

void nqueens(int row, int n) {

        for(int col=1; col<=n; col++) {
                if(place(row,col)) {
                        pos[row] = col;
                        if(row == n)
                        printf("%d%d%d%d\n",pos[4],pos[1],pos[2],pos[3]);
                        else
                        nqueens(row+1,n);
                }
        }
return;
}

int main(int argc, char *argv[]) {
        nqueens(1,8);
return 0;
}
