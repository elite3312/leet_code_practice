class Solution:
    def maxSubArray(self, nums):
        #dp[i]: maximum sub array that ends at i
        n=len(nums)
        dp=[None]*n
        dp[0]=nums[0]
        curr_max=nums[0]
        
        for i in range(1,n):
            dp[i]=max(nums[i],dp[i-1]+nums[i])
            curr_max=max(dp[i],curr_max)
        return curr_max


if __name__ == "__main__":

    s = Solution()
    
    ans = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(ans)
