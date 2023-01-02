class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        anchor=0
        while True:
            if (nums[anchor+1]+nums[anchor+2])>nums[anchor]:
                return nums[anchor+1]+nums[anchor+2]+nums[anchor]
            else:
                anchor+=1
                if (anchor+2)>=len(nums):return 0
        
if __name__=="__main__":
    s=Solution()
    nums = [2,1,2]
    #Output: 5
    nums = [1,1,2]
    #Output: 0
    ans = s.largestPerimeter(nums)
    print(ans)