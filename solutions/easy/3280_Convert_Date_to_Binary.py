from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# import math
# import heapq

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year,month,date=date.split('-')
        year=bin(int(year))[2:]
        month=bin(int(month))[2:]
        date=bin(int(date))[2:]
        return year+'-'+month+'-'+date
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [["2080-02-29"], "100000100000-10-11101"],

    ]

    test_driver_main(sol.convertDateToBinary, tests, index)
