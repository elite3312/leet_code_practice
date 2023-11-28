from utils.test_driver import test_driver
class Solution:  
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1 for _ in n]
        for i in range(n):
            for j in range(i):  
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
if __name__ == "__main__":
    s=Solution()
    tests=[
        [[10,9,2,5,3,7,101,18],4],
        [[10],1],
        [[10,10,10],1],
        [[10,11,12],3],
        [[4,10,4,3,8,9],3]
    ]
    for a,b in tests:
        test_driver(s.lengthOfLIS,a,expected=b)