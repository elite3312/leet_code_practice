from utils.test_driver import test_driver




class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        one=nums[0]
        nums=nums[1:]
        
        nums.sort()
        return one+nums[0]+nums[1]

        
if __name__ == "__main__":
    s = Solution()

    tests = [
            [  # case 1
                # inputs
                [
                    [2, 1, 3]
                ],
                # res
                6

            ],
       

    ]
    for input, res in tests:
        test_driver(s.minimumCost, input[0], expected=res)
'''
idea
first + first and seconde largest in nums[1:]
'''