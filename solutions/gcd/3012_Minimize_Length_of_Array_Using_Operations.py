from utils.test_driver import test_driver

from collections import Counter
class Solution:
   
    def minimumArrayLength(self, nums: list[int]) -> int:
        nums.sort()
        
        cnt = 1
        for num in nums[1:]:
            if num == nums[0]: cnt += 1
            else: 
                if num % nums[0] != 0: return 1
        return (cnt+1)//2




        

        
if __name__ == "__main__":
    s = Solution()

    tests = [
            [  # case 1
                # inputs
                [
                   [1,4,3,1]
                ],
                # res
                1

            ],
            [  # case 2
                # inputs
                [
                   [5,5,5,10,5]
                ],
                # res
                2

            ],
            [  # case 3
                # inputs
                [
                   [2,3,4]
                ],
                # res
                1

            ],
       

    ]
    for input, res in tests:
        test_driver(s.minimumArrayLength, input[0], expected=res)
