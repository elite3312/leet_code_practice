from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
#from itertools import combinations
# from collections import Counter
# from collections import deque

class Solution:
    def countSeniors(self, details: list[str]) -> int:
        res=0
        for d in details:
            age=int(d[11:13])
            if age>60:
                res+=1
        return res
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [
            [["7868190130M7522","5303914400F9211","9273338290F4010"]],2
        ]
    ]

    test_driver_main(sol.countSeniors, tests, index)
