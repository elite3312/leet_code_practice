from cmath import inf


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''
        greedy
        '''
        n=len(prices)
        if n ==1:return 0

        curr_min=inf
        res=0
        for i in range(1,n):
            if prices[i-1]<curr_min:
                curr_min=prices[i-1]
            res=max(res, prices[i]-curr_min)
        return res
    def maxProfit_dp(self, prices: list[int]) -> int:
        '''
        define dp[i]: best profit in interval(0,i)
            0 1 2 3 4 5
        P | 7 1 5 3 6 4

        then, 
        dp[0]=0
        dp[1]=max(dp[0],P[1]-min(P[0:1]))
        dp[2]=max(dp[1],P[2]-min(P[0:2]))
        ...
        '''
        n=len(prices)
        dp=[0 for _ in range(n)]
        dp[0]=0
        curr_min=prices[0]
        for i in range(1, n):
            if prices[i]<curr_min:curr_min=prices[i]
            dp[i]=max(dp[i-1],prices[i]-curr_min)
        return dp[n-1]
def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.maxProfit(input1)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)



if __name__ == "__main__":

    s = Solution()
    
    '''
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    '''
    test_driver(s,[7,1,5,3,6,4],None,5)