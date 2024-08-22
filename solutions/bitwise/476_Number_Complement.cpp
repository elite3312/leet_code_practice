#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstring>
#include <math.h>
#include <map>
#include <bitset>
using namespace std;
/**copy from here**/
class Solution {
public:
    int getBits(int num){
        //num>=1
        int bits=0;
        while (num!=0){
            bits+=1;
            num>>=1;
        }
        return bits;
    }
    int findComplement(int num) {
        //get bitlen, then flip the rightmost such bits with a mask and xor
        int bits=getBits(num),mask=1;
        while (bits--){
            num^=mask;
            mask<<=1;
        }
        return num;
    }
};
/**copy to here**/
int main()
{
    Solution *s = new Solution();
    int n;
    n=2;
    cout<<s->findComplement(n)<<endl;//1
    n=5;
    cout<<s->findComplement(n)<<endl;//2
    n=1;
    cout<<s->findComplement(n)<<endl;//0
    n=2147483647;
    cout<<s->findComplement(n)<<endl;//0
    
    return 0;
}
