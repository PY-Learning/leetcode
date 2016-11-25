/*************************************************************************
	> File Name: main.c
	> Author: 
	> Mail: 
	> Created Time: 2016年11月25日 星期五 11时29分49秒
 ************************************************************************/

#include<stdio.h>

int minimumTotal(int** triangle, int triangleRowSize, int *triangleColSizes) {
    int i, j;
    for(i=triangleRowSize-1; i>0; i--){
        for(j=0;j<i;j++){
            if(triangle[i][j] < triangle[i][j+1])
                triangle[i-1][j]+= triangle[i][j];
            else
                triangle[i-1][j]+= triangle[i][j+1];
        }
    }
    return triangle[0][0];
}
