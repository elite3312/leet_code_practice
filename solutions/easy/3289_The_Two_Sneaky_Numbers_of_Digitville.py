from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
from collections import Counter
# from collections import deque
# import math
# import heapq
class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        cnter=Counter(nums)
        res=[]
        for k in cnter:
            if cnter[k]>1:
                res.append(k)
        return res
        
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        

    ]

    test_driver_main(sol.getSneakyNumbers, tests, index)
