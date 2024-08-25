from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
from collections import defaultdict
class Solution:
    def countPairs(self, nums: list[int]) -> int:
        
        res=0
        
        # store ans
        _set=set()

        # setup hashmap
        hm=defaultdict(list)
        for i,s in enumerate(nums):
            hm[str(s)].append(i)

        for i,s in enumerate(nums):
            m=len(str(s))
            for j in range(m):
                for k in range(j,m):
                    neighbor=list(str(s))
                    temp=neighbor[j]
                    neighbor[j]=neighbor[k]
                    neighbor[k]=temp
                    neighbor=''.join(neighbor)
                    neighbor=neighbor.lstrip('0')

                    if len(hm[neighbor])>0:
                        for l in hm[neighbor]:
                            if i==l:continue
                            _sorted_tuple=tuple(sorted([i,l]))
                            _set.add(_sorted_tuple)
        res+=len(_set)
        return res
        
if __name__ == "__main__":

    sol = Solution()

    index = 0

    tests = [
        [[[3,12,30,17,21]],2],
        [[[1,1,1,1,1]],10],
        [[[123,231]],0],
        [[[1,1]],1],
        [[[1,3]],0],
    ]

    test_driver_main(sol.countPairs, tests, index)
