from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# import math
import heapq


class Solution:
    def resultsArray(self, queries: list[list[int]], k: int) -> list[int]:
        min_heap = []
        res = []
        for q in queries:
            num = abs(q[0])+abs(q[1])
            num = -num
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

            if len(min_heap) == k:
                res.append(-min_heap[0])
            else:
                res.append(-1)

        return res


if __name__ == "__main__":

    sol = Solution()

    index = 0

    tests = [
        [[[[1, 2], [3, 4], [2, 3], [-3, 0]], 2], [-1, 7, 5, 3]],
        [[[[5, 5], [4, 4], [3, 3]], 1], [10, 8, 6]],

    ]

    test_driver_main(sol.resultsArray, tests, index)
