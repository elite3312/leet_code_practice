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
    int minSteps(int n) {
        

        int dp[1001];
        for (int i=0;i<1001;++i)dp[i]=INT_MAX;
        dp[1]=0;//nothing
        //dp[2]=2;//c p
        //dp[3]=3;//c p p
        //dp[4]=4;//c p c p, 
        //dp[5]=5;//c p p p p
        //dp[6]=5;//c p p c p
        //dp[7]=7;//c p p p p p p
        //dp[8]=6;//c p c p c p
        //dp[9]=5;//c p p c p p
        for (int i=2;i<=n;++i){
            for (int j=1;j*j<=i;++j){
                if (i %j==0)
                {
                    dp[i]=min(dp[i],dp[j]+i/j);//start with j As, copy then paste (i/j)-1 times 
                    if (j*j != i)
                        dp[i] = min(dp[i], dp[i / j] +j);//start with (i/j)As, copy then paste j-1 times
                }
            }
        }
        return dp[n];
    }
};
/**copy to here**/
int main()
{
    Solution *s = new Solution();
    int n=3;
    cout<<s->minSteps(n)<<',';//3
    n=1;
    cout<<s->minSteps(n)<<',';//0
    n=6;
    cout<<s->minSteps(n)<<',';//5
    n=15;
    cout<<s->minSteps(n)<<',';//8
    n=25;
    cout<<s->minSteps(n)<<',';//10
    n=247;
    cout<<s->minSteps(n)<<',';//10
    return 0;
}
