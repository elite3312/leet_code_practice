
from utils.test_driver import test_driver
from itertools import combinations
import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n=len(arr)
        if k<n-1:
            return [1,arr[-k]]
        '''
        1     ,3     ,5     ,...,13
        arr[0],arr[1],arr[2],...,arr[n-1]
        0th smallest: 1/arr[n-1]
        (n-2)th smallest: 1/arr[1]
        '''
        combs=combinations(arr,2)
        h=[]
        for c in combs:
            h.append((c[0]/c[1],(c[0],c[1]))) 
        heapq.heapify(h)

        for i in range(k):
            cur=heapq.heappop(h)
            if i==k-1:
                return list(cur[1])


if __name__ == "__main__":
    s = Solution()

    index = 0

    arr = [1,2,3,5]
    k = 3
    res = [2,5]
    tests = [
        [#0
            [
                arr, k
            ],
            res
        ],
        [#1
            [
                [1,7], 1
            ],
            [1,7]
        ]

    ]

    for input, res in tests[index:]:
        test_driver(s.kthSmallestPrimeFraction, input[0],input[1], expected=res)
