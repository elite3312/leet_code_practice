class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)


if __name__ == "__main__":

    s = Solution()
    
    ans = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(ans)
