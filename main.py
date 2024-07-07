from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottles_left=numBottles

        res=0

        res+=bottles_left
        bottles_left=bottles_left/numExchange+bottles_left%numExchange

        while full_bottles_left>numBottles
if __name__ == "__main__":
    sol = Solution()

    index = 2

    tests = [
        [[9,3],
         13
         ],
      
    ]

    test_driver_main(sol.numWaterBottles, tests, index)
