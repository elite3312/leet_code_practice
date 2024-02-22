/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>
int hammingWeight(short int n) {
    int res=0;
    int bit_size=sizeof(n)*8;
    while(bit_size){
        if(n%2)res++;
        n>>=1;
        bit_size--;
    }
    return res;
}
/*
int hammingWeight(uint32_t n) {
    int res=0;
    int bit_size=sizeof(n)*8;
    while(bit_size){
        if(n%2)res++;
        n>>=1;
        bit_size--;
    }
    return res;
}
*/
int main()
{
	
	short int a=0x5;//2
    printf("%d",hammingWeight(a));
	return 0;
}

