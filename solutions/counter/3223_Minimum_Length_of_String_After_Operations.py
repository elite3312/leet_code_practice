from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
from collections import Counter
# from collections import deque
# import math
# import heapq
class Solution:
    def minimumLength(self, s: str) -> int:
        n=len(s)
    
        cnter=Counter(s)
        
        remove_cnt=0
        
        for k,v in cnter.items():
            if v>=3:
                while v>2:
                    remove_cnt+=2
                    v-=2
        return n-remove_cnt
        
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [["abaacbcbb"],5],
        [["aa"],2]

    ]

    test_driver_main(sol.minimumLength   , tests, index)
