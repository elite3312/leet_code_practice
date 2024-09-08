from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# import math
# import heapq

class Solution:
    def maxPossibleScore(self, start: list[int], d: int) -> int:
        # we want the picked values to 
        # spread out as much as possible.
        # We can use binary search to search for the distance between each picked values.

        start.sort()# we need the array to be sorted to apply binary search
        n=len(start)

        def check(mid):
            # this function checks if we can in fact 
            # reach all intervals using this mid
            
            nonlocal start,d,n
            prev=start[0]
            for i in range(1,n):
                _next=max(prev+mid,start[i])
                if _next>start[i]+d:#太遠
                    return False
                else:# 夠近或是不夠
                    prev=_next
            return True

        # Use binary search to find the largest possible 
        # minimum difference (mid) between consecutive values
        low,hi=0,(start[-1]+d)-start[0]
        while(low<=hi):
            mid=(low+hi)//2
            if check(mid):
                res=mid
                low=mid+1
            else:
                hi=mid-1
        return res
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[[6,0,3],2], 4],
        [[[2,6,13,13],5],5]

    ]

    test_driver_main(sol.maxPossibleScore, tests, index)
