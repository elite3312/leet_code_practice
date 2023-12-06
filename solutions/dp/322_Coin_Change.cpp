#include <iostream>
#include <vector>
#include "utils/TestDriver.hpp"

using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount==0)return 0;
        int n=coins.size();

        int dp[12][10001]={0};
        int Inf = 1e9;  
        for (int j =0 ;j<amount+1;j++){
            dp[0][j]=j%coins[0]!=0 ? Inf:j/coins[0];
        }
        for (int i =1;i<n;i++)
            for (int j=1 ;j <amount+1;j++){
                if (coins[i]<=j)
                    dp[i][j]=min(dp[i-1][j],dp[i][j-coins[i]]+1);
                else
                    dp[i][j]=dp[i-1][j];
            }
        int curr_min=Inf;
        for (int i =0;i<n;i++){
            curr_min=min(curr_min,dp[i][amount]);
        }
        return  curr_min==Inf ?-1: curr_min;
    }
};
int main (){
    Solution *s=new Solution();
    vector<int> v={1,2,5};

    int res=0;
    res=s->coinChange(v,100);
    
    return 0;
}