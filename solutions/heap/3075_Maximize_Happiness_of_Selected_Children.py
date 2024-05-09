
from utils.test_driver import test_driver

import heapq
class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        n=len(happiness)
        for i in range(n):
            happiness[i]*=-1
        heapq.heapify(happiness)

        res=0
        
        for i in range(k):
            cur=-heapq.heappop(happiness)
            cur-=i
            if cur<0:cur=0
            res+=cur
        return res



if __name__ == "__main__":
    s = Solution()

    index = 0

    happiness = [1, 2, 3]
    k = 2
    res = 4
    tests = [
        [#0
            [
                happiness, k
            ],
            4
        ],
        [#1
            [
                [1,1,1,1], 2
            ],
            1
        ]

    ]

    for input, res in tests[index:]:
        test_driver(s.maximumHappinessSum, input[0],input[1], expected=res)
