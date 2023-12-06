from utils.test_driver import test_driver
from cmath import inf
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount==0:return 0
        n=len(coins)
        
        dp=[[0 for _ in range(amount+1)]for _ in range(n)]#dp[r,c]=min coins using 1st r coins to create amount c

        for j in range(amount+1):
            dp[0][j]=inf if j %coins[0]!=0 else j//coins[0]
        for i in range(1,n):
            for j in range(1,amount+1):
                if coins[i]<=j:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-coins[i]]+1)
                else:
                    dp[i][j]=dp[i-1][j]
        curr_min=inf
        for i in range(n):
            curr_min=min(curr_min,dp[i][amount])
        return -1 if curr_min==inf else curr_min

# idea: use a 2D dp.
# dp[i][j]=minimum coins needed to sum to amount j using first 1 coins.
# dp[i][j]=min(dp[i-1][j],dp[i][j-coins[i]]+1), provided j-coins[i] >=0.
# we fill up the table like this:
#       0 1 2 3 4 5 6 7 8
# [1] 0 0 1 2 3 4 5 6 7 8
# [2] 1 0 1 1 2 ...
# [5] 2 
#
# note that for each dp[i]. dp[i][0]=0, since we need 0 coins to create value 0



        
if __name__ == "__main__":
    s=Solution()
    tests=[
        [[[1,2,5],100],20],
        [[[1,2147483647],2],2],
        [[[186,419,83,408],6249],20],
        [[[2],3],-1],
        [[[1,2,5],11],3],
        [[[1],0],0],
    ]
    for a,b in tests:
        test_driver(s.coinChange,a[0],a[1],expected=b)