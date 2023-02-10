class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        #dp=[i][j]#maximum subarray in both nums1[0:i] and nums2[0:j]
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        res=0
        for i in range(1,len(nums1)+1):
            for j in range(1,len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    res=max(res,dp[i][j])
        return res
        
if __name__ == "__main__":
    
    s = Solution()
    nums1=[250,145,147,145,145]
    nums2=[240,162,138,147,145,17]
    ans=s.findLength(nums1,nums2)
    print(ans)
    