from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# import math
# import heapq
class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        '''
        arr1:fed
        arr2:cba

        a^b a^e a^f
        b^d b^e b^f
        c^d c^e c^f

        the insight:

        we see that for each elem in arr2, for example 'a', its contribution to the final answer
        if affected by the len of arr1.
        '''
        res=0

        n,m=len(nums1),len(nums2)

        if (m % 2 )==1:
            for e in nums1:
                res=res^e
        if (n % 2 )==1:
            for e in nums2:
                res=res^e
        return res
        
        
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[[2,1,3],[10,2,5,0]],13],
        [[[1,2],[3,4]],0]

    ]

    test_driver_main(sol.xorAllNums   , tests, index)
