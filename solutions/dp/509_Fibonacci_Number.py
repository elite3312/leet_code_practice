from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# import math
# import heapq

class Solution:
    def fib(self, n: int) -> int:

        def dp(n):
    
            ## look-up table
            if n in table:
                return table[n]

            ## general cases
            # DP[n] = DP[n-1] + DP[n-2]

            table[n] = dp(n-1) + dp(n-2)

            return table[n]

        # ---------------------------------

        # base case
        # DP[0] = 0
        # DP[1] = 1
        table = {0:0, 1:1}

        return dp(n)

if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [   [0],0],
        [[1],1],
        [[2],1],
        [[3],2],
        [[4],3],
        [[5],5],
        [[6],8],
        [[7],13],
        [[8],21],
        [[9],34],
        [[10],55],
        [[20],6765],
        [[30],832040],
        [[35],9227465],
        [[36],14930352],
        [[37],24157817],
        [[38],39088169],
        [[39],63245986],
        [[40],102334155],
    ]

    test_driver_main(sol.fib   , tests, index)
