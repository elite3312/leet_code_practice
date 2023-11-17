class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:return nums[0]
        elif len(nums)==1:return max(nums[0],nums[1])
        nums_l=nums[:len(nums)-1]
        nums_r=nums[1:]

        return max(self.find_max(nums_l),self.find_max(nums_r))
    def find_max(self,nums):
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

                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()
    nums = [2,2,4,3,2,5]
    output=10
    test_driver(s.rob,nums,expected=output)

    nums = [1,1,1,2]
    output=3
    test_driver(s.rob,nums,expected=output)

    nums=[2,1,1,2]
    output=3
    test_driver(s.rob,nums,expected=output)

    nums = [2,3,2]
    output=3
    test_driver(s.rob,nums,expected=output)

    nums = [2,3,2,10]
    output=13
    test_driver(s.rob,nums,expected=output)

    nums = [1,2,3,1]
    output=4
    test_driver(s.rob,nums,expected=output)

    nums = [1,2,3]
    output=3
    test_driver(s.rob,nums,expected=output)

    # idea: call the dp method in house robber 1, and run it on nums[0:len(nums)-1] and nums[1:]