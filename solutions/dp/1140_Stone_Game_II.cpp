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
    int getMaxStones(int n,vector<int>&  piles,vector<int>& suffixSum,int dp[101][101],int i,int M)
    {
        
        if(i==n)//base case : reached the end
        {
            return 0;
        }
        if(2*M>=n-i)//base case : alice takes all remaining piles
        {
            return suffixSum[i];
        }
        if(dp[i][M]>0)//dp[i][m] exists
        {
            return dp[i][M];
        }
        int minStonesForBob=INT_MAX;
        for(int X=1;X<=2*M;X++)
        {
             //bob is simply another player playing by the same rules,
             //so we can call getMaxStones for Bob
             minStonesForBob=min(minStonesForBob,getMaxStones(n,piles,suffixSum,dp,i+X,max(M,X)));
        }
        dp[i][M]=suffixSum[i]-minStonesForBob;
        return dp[i][M];
    }
    int stoneGameII(vector<int>& piles) {
        int n=piles.size();
        if(n==1)return piles[0];
        
        /*
        dp[i][M] : what alice can gan from remaining piles when value is M.
        base cases
        if i==n, we have reached the end so return 0
        if M*2>=(n-i), alice can take all remaining piles, so return suffixSum[i]
        */
        
        /*
        Recursion for Dynamic Programming Calculation:
        Try every possible X (number of piles Alice can take) where 1 <= X <= 2 * M.
        Calculate the minimum stones Bob can get using recursive calls.
        Update dp[i][M] with the maximum stones Alice can get, which is suffixSum[i] - minStonesForBob
        */

        vector<int> suffixSum(n,0);
        suffixSum[n-1]=piles[n-1];
        for(int i=n-2;i>=0;i--)
        {
            suffixSum[i]=suffixSum[i+1]+piles[i];
        }

        int dp[101][101]={0};//ixm
        return getMaxStones(n,piles,suffixSum,dp,0,1);
    }
};
/**copy to here**/
int main()
{
    Solution *s = new Solution();
    vector<int> piles = {2,7,9,4,4};//10
    /*2 7 9 4 4
      A B B A A
      A A B B B    
    */
    cout<<s->stoneGameII(piles)<<endl;
    return 0;
}
