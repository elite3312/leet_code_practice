from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# import math
# import heapq

'''
You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.

You are also given an integer array nums of length n and an integer maxDiff.

An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).

You are also given a 2D integer array queries. For each queries[i] = [ui, vi], find the minimum distance between nodes ui and vi. If no path exists between the two nodes, return -1 for that query.

Return an array answer, where answer[i] is the result of the ith query.

Note: The edges between the nodes are unweighted.
'''

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        # let idx[i] denote the original index of the i-th element in the sorted array.
        idx = sorted(range(n), key=lambda i: nums[i])# sort the indices of nums by their values nums[i]

        #Let pos[j] denote the position of nums[j] in the sorted array
        pos = [0] * n
        for i, j in enumerate(idx):
            pos[j] = i

        # These two arrays provide a bidirectional mapping between the original and sorted orders.

        # binary lifting
        # Let f[x][i] denote the node reached after making 2 i
        # leftward jumps from node x, where 0≤i≤⌊log 2n⌋
        m = n.bit_length()
        f = [[0] * m for _ in range(n)]

        left = 0
        for i in range(n):
            while left < i and nums[idx[i]] - nums[idx[left]] > maxDiff:
                left += 1
            f[i][0] = left

        for j in range(1, m):
            for i in range(n):
                f[i][j] = f[f[i][j - 1]][j - 1]

        res = []
        for query in queries:
            x, y = pos[query[0]], pos[query[1]]
            if x > y:
                x, y = y, x

            if x == y:
                res.append(0)
                continue

            step = 0
            for i in range(m - 1, -1, -1):
                if f[y][i] > x:
                    y = f[y][i]
                    step += 1 << i

            if f[y][0] <= x:
                res.append(step + 1)
            else:
                res.append(-1)

        return res

if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[5,[1,8,3,4,2],3,[[0,3],[2,4]]],#input
         [1,1]#answer
         ],
       
    ]

    test_driver_main(sol.pathExistenceQueries   , tests, index)
