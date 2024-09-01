from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# import math

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # black: odd, odd or even, even
        parity_1=(ord(coordinate1[0])-ord('a')+1)%2
        parity_2=(ord(coordinate1[1])-ord('1')+1)%2
        
        
        color_1='white'
        if (parity_1==parity_2):
            color_1='black'

        parity_1=(ord(coordinate2[0])-ord('a')+1)%2
        parity_2=(ord(coordinate2[1])-ord('1')+1)%2
        
        
        color_2='white'
        if (parity_1==parity_2):
            color_2='black'
        return color_1==color_2

if __name__ == "__main__":

    sol = Solution()

    index = 0

    tests = [
        [["a1","c3"], True],
         [["a1","h3"], False],
       
    ]

    test_driver_main(sol.checkTwoChessboards, tests, index)
