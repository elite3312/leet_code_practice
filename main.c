/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>
int* runningSum(int* nums, int numsSize, int* returnSize){
    *returnSize=numsSize;
    for(int i=1;i<numsSize;i++){
            nums[i]=nums[i-1]+nums[i];

        }
    return nums;
}

int main()
{
	
	int nums[3]={1,2,3};
    int returnSize;
    int *ret;
    ret=runningSum(nums,3,&returnSize);
    for(int i=0;i<returnSize;i++)printf("%d ",ret[i]);
	return 0;
}

