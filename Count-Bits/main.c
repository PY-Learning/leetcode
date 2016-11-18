/**

 * Return an array of size *returnSize.

 * Note: The returned array must be malloced, assume caller calls free().

 */

int* countBits(int num, int* returnSize) 
{
    int* ret = malloc((num + 1) * sizeof(int));
    ret[0] = 0;
    for(int i=1;i<=num;i++){
        ret[i] = (ret[i>>1] + (i&1));
    }
    *returnSize = num+1;
    return ret;
}
