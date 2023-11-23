class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        expected_sum=(1+n)*n/2
        real_sum=0
        for num in nums:
            real_sum+=num
        return int(expected_sum-real_sum)

                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()

    inp= [0,2,3]
    out=1
    test_driver(s.missingNumber,inp,expected=out)

    inp= [0]
    out=1
    test_driver(s.missingNumber,inp,expected=out)

    inp= [1]
    out=0
    test_driver(s.missingNumber,inp,expected=out)
# idea : use the summation formula to get the expected_sum. then add all numbers in nums to get real sum. the difference is the answer.