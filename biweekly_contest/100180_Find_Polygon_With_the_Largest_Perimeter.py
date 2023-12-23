from utils.test_driver import test_driver


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        curr_largest_index=n-1
        curr_sum_excluding_largest=sum(nums[:curr_largest_index])
        while 1:
            if curr_largest_index<=1:break
            curr_largest=nums[curr_largest_index]
            if curr_largest<curr_sum_excluding_largest:
                return curr_largest+curr_sum_excluding_largest
            # else
            curr_largest_index-=1
            curr_sum_excluding_largest-=nums[curr_largest_index]
        return -1


if __name__ == "__main__":
    s = Solution()

    tests = [
            [[1,12,1,2,5,50,3],12],
            [[5,5,5],15],
            [[5,5,50],-1],
        ]
    for input, res in tests:
        test_driver(s.largestPerimeter, input, expected=res)
