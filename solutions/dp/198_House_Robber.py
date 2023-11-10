'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 
'''
class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[0 for i in range(len(nums))]# dp[i] = maximum value from 0 to i
        # base case
        dp[0]=nums[0]
        if len(nums)==1:return nums[0]
        dp[1]=max(nums[:2])
        if len(nums)==2:return dp[1]

        curr_max=0
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])# either you take item i and dp[i-2], or you take dp[i-1] and leave item i
            curr_max=max(dp[i],curr_max)
        return curr_max

def test_driver(s: Solution, *inputs, expected: str):
    # change this line
    ans = s.rob(*inputs)

    for i in range(len(inputs)):
        print('input_%d : %s'%(i,str(inputs[i])))
    print("ans: ", ans)
    print('expected:', expected)
if __name__ == "__main__":
    s = Solution()

    # change below
    nums = [1,2,3,1]
    ans=4
    test_driver(s,nums,expected=ans)

    nums = [2,7,9,3,1]
    ans= 12
    test_driver(s,nums,expected=ans)