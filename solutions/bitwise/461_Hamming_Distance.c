
#include <stdio.h>
#include <stdlib.h>
int hammingDistance_(int x, int y) {
    unsigned short bit_len=8*sizeof(int);
    int res=0;
    while (bit_len--)
    {
        if(x&1!=y&1)res++;
        x>>=1;
        y>>=1;
        if(x==0&&y==0)break;
    }
    return res;
    
}
int hammingDistance(int x, int y) {
    int n=x^y;
    int res=0;
    int bit_size=sizeof(n)*8;
    while(bit_size){
        if(n&1)res++;
        n>>=1;
        bit_size--;
    }
    return res;
}
int main()
{
	
	int a,b;

    a=1,b=4;//2
    printf("%d",hammingDistance(a,b));

    a=3,b=1;//1
    printf("%d",hammingDistance(a,b));

	return 0;
}
