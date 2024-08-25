from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        n=len(nums)
        for i in range (k):
            curMin=1e9
            curMinIndex=-1
            for j in range(n-1,-1,-1):
                if nums[j]<=curMin:
                    curMin=nums[j]
                    curMinIndex=j
            nums[curMinIndex]*=multiplier
        return nums
        
        
if __name__ == "__main__":

    sol = Solution()

    index = 0

    tests = [
        [[[2,1,3,5,6],5,2],[8,4,6,5,6]],
        
    ]

    test_driver_main(sol.getFinalState, tests, index)
