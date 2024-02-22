
#include <stdio.h>
#include <stdlib.h>
int hammingDistance(int x, int y) {
    unsigned short bit_len=8*sizeof(int);
    int res=0;
    while (bit_len--)
    {
        if(x%2!=y%2)res++;
        x>>=1;
        y>>=1;
        if(x==0&&y==0)break;
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
