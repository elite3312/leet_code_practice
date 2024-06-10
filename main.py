from utils.test_driver import test_driver_main


# from collections import Counter
# from collections import deque 

class Solution:
    def maxTotalReward(self, rewardValues: list[int]) -> int:
        # sort+dp+prefix_sum?

        n=len(rewardValues)

        # sort
        rewardValues.sort()

        # pref sum
        pref_sum=[0]
        pref_sum[0]=rewardValues[0]
        for i in range(1,n):
            pref_sum[i]=pref_sum[i-1]+rewardValues[i]

        dp=[0 for _ in range(n)]
        dp[0]=rewardValues[0]

        for i in range(1,n):
            dp[i]=max(pref_sum[i-1])
            


if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [
            [1,1,3,3],#1,3
            4
        ],
        [
            [1,6,4,3,2],#1,4,6
            11
        ],
        
    ]

    test_driver_main(sol.maxTotalReward,tests,index)
