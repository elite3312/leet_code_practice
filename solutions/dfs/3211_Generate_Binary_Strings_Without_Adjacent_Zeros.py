from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
class Solution:
    def validStrings(self, n: int) -> list[str]:
        res=[]
        def inner(cur_s):
            if len(cur_s)==n:
                res.append(cur_s)
            elif cur_s=='':
                inner(cur_s+'0')
                inner(cur_s+'1')
            else:
                if cur_s[-1]=='0':
                    inner(cur_s+'1')
                else:
                    inner(cur_s+'0')
                    inner(cur_s+'1')
        inner("")
        return res


if __name__ == "__main__":
    sol = Solution()

    index =0

   
    tests=[
        [[3],
        ["010","011","101","110","111"]
        ],
        
    ]

    test_driver_main(sol.validStrings, tests, index)
