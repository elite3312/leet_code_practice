from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# import math
# import heapq
class Solution:
    def maxScore(self, a: list[int], b: list[int]) -> int:
        res=[-float('inf'),-float('inf'),-float('inf'),-float('inf')]
        for e in b:
            res[3]=max(res[3],res[2]+a[3]*e)
            res[2]=max(res[2],res[1]+a[2]*e)
            res[1]=max(res[1],res[0]+a[1]*e)
            res[0]=max(res[0],a[0]*e)
        return res[3]
        
            
        
        
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[[3,2,5,6],[2,-6,4,-5,-3,2,-7]],26]

    ]

    test_driver_main(sol.maxScore   , tests, index)
