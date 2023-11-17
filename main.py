class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[0 for i in range(len(nums))]# dp[i] = maximum value from 0 to i
        is_first_taken=[0 for i in range(len(nums))]# is the first house robbed for dp[i]

        # base case
        dp[0]=nums[0]
        is_first_taken[0]=1
        if len(nums)==1:return nums[0]
        
        dp[1]=max(nums[:2])
        if dp[1]==nums[0]:is_first_taken[1]==1
        if len(nums)==2:return dp[1]

        curr_max=0
        for i in range(2,len(nums)-1):
            # either you take item i and dp[i-2], or you take dp[i-1] and leave item i
            if dp[i-2]+nums[i]>dp[i-1]:
                is_first_taken[i]=is_first_taken[i-2]
                dp[i]=dp[i-2]+nums[i]
            else:
                is_first_taken[i]=is_first_taken[i-1]
                dp[i]=dp[i-1]
            curr_max=max(dp[i],curr_max)
        
        i=len(nums)-1
        if dp[i-2]+nums[i]>dp[i-1]:
            if is_first_taken[i-2]:
                dp[i]=max(dp[i-2],nums[i])
            else:
                dp[i]=dp[i-2]+nums[i]
        else:
            dp[i]=dp[i-1]

        return curr_max
                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()
    nums = [2,3,2]
    output=3
    test_driver(s.rob,nums,expected=output)

    nums = [2,3,2,10]
    output=13
    test_driver(s.rob,nums,expected=output)