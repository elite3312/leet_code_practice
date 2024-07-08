from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res=numBottles

        empty_bottles_left=numBottles

        while empty_bottles_left>=numExchange:
            full_bottles_left=empty_bottles_left//numExchange
            res+=full_bottles_left
            empty_bottles_left=full_bottles_left+empty_bottles_left%numExchange
        return res
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[9,3],
         13
         ],
      
    ]

    test_driver_main(sol.numWaterBottles, tests, index)
