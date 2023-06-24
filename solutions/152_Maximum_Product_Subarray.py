class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        currMaxProductSubarr = nums[0]# the maximum product of a subarray that ends at the current index
        currMinProductSubarr = nums[0]# the minimum product of a subarray that ends at the current index
        maxProductAns = nums[0]# maximum product obtained so far
        for i in range(1, n):
            temp = currMaxProductSubarr
            currMaxProductSubarr = max(nums[i], max(currMaxProductSubarr * nums[i], currMinProductSubarr * nums[i]))
            currMinProductSubarr = min(nums[i], min(temp * nums[i], currMinProductSubarr * nums[i]))
            maxProductAns = max(maxProductAns, currMaxProductSubarr)
        return maxProductAns
def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.maxProduct(input1)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)



if __name__ == "__main__":

    s = Solution()
    
    
