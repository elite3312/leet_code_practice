from cmath import inf
from utils.test_driver import test_driver
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n=len(coins)
        
        dp=[[0 for _ in range(n)]for _ in range(amount+1)]#dp[r,c]=min coins using 1st r coins to create amount c

        for j in range(amount+1):
            dp[0][j]=-1 if j %coins[0]!=0 else dp[0][j]//coins[0]
        curr_min=inf
        for i in range(1,n):
            for j in range(1,amount+1):

                dp[i][j]=min(dp[i-1][j],dp[i][j-1]+1)
                curr_min=min(curr_min,dp[i][j])
        return curr_min



        
if __name__ == "__main__":
    s=Solution()
    tests=[
        [[[1,2,5],11],3],
        [[[2],3],-1],
        [[[1],0],0],
    ]
    for a,b in tests:
        test_driver(s.coinChange,a[0],a[1],expected=b)