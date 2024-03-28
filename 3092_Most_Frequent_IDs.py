from utils.test_driver import test_driver

from collections import Counter
from heapq import heappop,heappush
class Solution:
    def mostFrequentIDs(self, nums: list[int], freq: list[int]) -> list[int]:
        h = []
        count = Counter()
        res = []
        for i, f in zip(nums, freq):
            count[i] += f
            heappush(h, [-count[i], i])
            #while heaptop' count[key] does not match the freq of heap top, pop from heap
            while count[h[0][1]] != -h[0][0]:
                heappop(h)
            res.append(-h[0][0])
        return res

        
if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                [5,5,3],[2,-2,1]
            ],
            # res
            [2,0,1]

        ],
        [
            # inputs
            [
                [2,3,2,1],[3,2,-3,1]
            ],
            # res
            [3,3,2,2]

        ],
    
    ]
    for input, res in tests:
        test_driver(s.mostFrequentIDs, input[0],input[1],  expected=res)
