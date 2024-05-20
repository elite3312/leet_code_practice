
from utils.test_driver import test_driver
class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        def get_parity(num):
            
            return num%2
        n=len(nums)
        prev_parity=get_parity(nums[0])
        for i in range(1,n):
            cur_parity=get_parity(nums[i])
            if cur_parity%2==prev_parity%2:return False

            prev_parity=cur_parity
        return True


        
              


if __name__ == "__main__":
    sol = Solution()

    index = 0

    nums = [1]
    res=True
    tests = [
        [#0
            [
            nums
            ],
            res
        ],
        [#1
            [
            [4,3,1,6]
            ],
            False
        ],
        [#2
            [
            [2,1,4]
            ],
           True
        ],
        [#3
            [
            [1,5]
            ],
           False
        ],
        [#4
            [
            [1,6]
            ],
           True
        ],
    ]

    for input, res in tests[index:]:
        test_driver(sol.isArraySpecial, input[0], expected=res)
