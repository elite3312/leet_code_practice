from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# import math
# import heapq


class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        pass
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[[[1,2,3],[4,3,2],[1,1,1]]], 8],
        [[[[8,7,6],[8,3,2]]],15]

    ]

    test_driver_main(sol.maxScore, tests, index)
