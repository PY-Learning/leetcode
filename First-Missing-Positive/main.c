/*************************************************************************
	> File Name: main.c
	> Author: 
	> Mail: 
	> Created Time: 2016年11月21日 星期一 12时30分54秒
 ************************************************************************/
#include<stdio.h>

int firstMissingPositive(int* nums, int numsSize) {
    int i=0, tmp;
    for(i=0;i<numsSize;i++)
    {
        if(nums[i] > 0 && nums[i]<numsSize)
        {
            if(nums[nums[i]-1] == nums[i]) continue;
            tmp = nums[nums[i]-1];
            nums[nums[i]-1] = nums[i];
            nums[i] = tmp;
            i--;
        }
    }

    for(i=0;i<numsSize;i++)
    {
        if(nums[i]-1 !=i) return i+1;
    }
    return i+1;
}

int main()
{
    int nums[] = {2, 3, 4};
    printf("%d", firstMissingPositive(nums, sizeof(nums)));
    return 0;
}
