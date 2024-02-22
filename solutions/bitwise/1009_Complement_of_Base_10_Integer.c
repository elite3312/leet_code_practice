
#include <stdio.h>
#include <stdlib.h>
int bitwiseComplement(int n){
    /*obtain bit index of left most bit(0 indexed)*/
    int bit_index=0,temp_n=n;
    // If n is 0, return (no bits are set)
    if (temp_n == 0)
        return 1;
    // Loop until the leftmost set bit is found
    while (temp_n != 0) {
        temp_n = temp_n >> 1; // Right shift by 1
        bit_index++;    // Increment index
    }
    bit_index--;

    /*invert the rightmost 'bit_index' bits*/
    int mask=0;
    while(1){
        bit_index--;
        mask+=1;
        if(bit_index<0)break;
        mask<<=1;
    }
    n=~n;
    n&=mask;
    
    return n;
}

int main()
{
	
	int a;

    a=5;//101-> 010 ->2
    printf("%d",bitwiseComplement(a));

    a=10;//5
    printf("%d",bitwiseComplement(a));

    a=7;//0
    printf("%d",bitwiseComplement(a));

	return 0;
}

/*
class Solution {
public:
    int bitwiseComplement(int n) {
        int m = n;
        if(m==0)return 1;
        int mask = 0 ;
        while(m!=0)
        {
            mask = (mask << 1) | 1;
            m = m >> 1;
        }
        int ans = (~n) & mask; 
        return ans;
    }
};
*/