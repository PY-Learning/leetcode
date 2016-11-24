/*************************************************************************
	> File Name: main.c
	> Author: 
	> Mail: 
	> Created Time: 2016年11月24日 星期四 11时45分29秒
 ************************************************************************/

#include<stdio.h>

int findPeakElement(int* nums, int numsSize) {
    int low = 0, high = numsSize - 1;
    while (low < high){
        //printf("%d, %d", low, high);
        int mid = low + (high-low) / 2;
        if (nums[mid] > nums[mid+1]){
            high = mid;
        }else{
            low = mid + 1;
        }
    }
    return low;
}

void main(){
    int nums[] = {1,2,3,1};
    int res;
    res = findPeakElement(nums, sizeof(nums)/sizeof(int));
    printf("%d", res);
}
