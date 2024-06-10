from utils.test_driver import test_driver_main


# from collections import Counter
# from collections import deque

class Solution:
    '''
    1 <= rewardValues.length <= 2000
    1 <= rewardValues[i] <= 2000
    '''
    def maxTotalReward(self, rewardValues: list[int]) -> int:
        n = len(rewardValues)
        if n == 1:
            return rewardValues[0]

        # sort
        rewardValues.sort()  # we are going to pick values from left to right
        res=0
        mx=rewardValues[-1]
        dp=[[-1 for j in range(mx+1)]for i in range(n)]
        def inner(cur,reward):
            if cur==n or reward>mx:return reward
            if dp[cur][reward]!=-1:return dp[cur][reward]
            res=dp[cur][reward]
            if rewardValues[cur]>reward:res=max(res,inner(cur+1,reward+rewardValues[cur]))
            res=max(res,inner(cur+1,reward))
            return res
        return inner(0,0)
    def maxTotalReward_tle(self, rewardValues: list[int]) -> int:
        '''this will currently cause tle'''
        # sort+dp+top down recursion
        '''
        We define state as: we are looking at index i, and we have already accumulated "state" as the sum. 
        '''

        n = len(rewardValues)
        if n == 1:
            return rewardValues[0]

        # sort
        rewardValues.sort()  # we are going to pick values from left to right

        # we can infer from the definition that maximum sum we may obtain is at most 3999
        # 1+1998+2000=3999

        max_elem=max(rewardValues)
        dp = [[-1 for j in range(max_elem+1)]for i in range(n)]
        # dp [i][j] = -1 if "the best sum when x is at j for index i" has not been computed
        # else dp[i][j] is the best sum we can later get when x is at j for index i

        def inner(cur_sum: int, cur_index: int):
            if cur_index >= n:
                return cur_sum
            if dp[cur_index][cur_sum] != -1:
                # if the best value for this state has been found, return it
                return dp[cur_index][cur_sum]
            # the best value has not been found yet
            value_from_not_pick = inner(
                cur_sum, cur_index+1)  # increment the index
            
            value_from_pick=-1
            if rewardValues[cur_index] > cur_sum:
                # then this means we are free to pick this value
                # and we increment the index
                value_from_pick = inner(
                    cur_sum+rewardValues[cur_index], cur_index+1)

            return max(value_from_not_pick, value_from_pick)

        return inner(0, 0)

if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [
            [[1, 1, 3, 3]],  # 1,3
            4
        ],
        [
            [[1, 6, 4, 3, 2]],  # 1,4,6
            11
        ],

    ]

    test_driver_main(sol.maxTotalReward, tests, index)
