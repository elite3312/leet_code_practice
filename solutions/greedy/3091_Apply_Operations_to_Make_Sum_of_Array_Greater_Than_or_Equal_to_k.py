from utils.test_driver import test_driver
from collections import Counter

'''
11/4 11/5 11/6

3   3   2
+   +   +
3   4   5
'''

class Solution:
    def minOperations(self, k: int) -> int:
        res=1e9
        cur=1
        if k<=cur:return 0
        while 1:
            cur_cost=cur-1+int(k/cur)
            if k%cur==0:
                cur_cost-=1
            
            res=min(res,cur_cost)
            cur+=1
            if cur>=k:
                res=min(res,cur-1)
                break
        return res
            
if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                5
            ],
            # res
            3

        ],
        [
            # inputs
            [
                4
            ],
            # res
            2

        ],
        [
            # inputs
            [
                3
            ],
            # res
            2

        ],
        [
            # inputs
            [
                2
            ],
            # res
            1

        ],
        [
            # inputs
            [
                11
            ],
            # res
            5

        ],
        [
            # inputs
            [
                1
            ],
            # res
            0

        ],

    ]
    for input, res in tests:
        test_driver(s.minOperations, input[0],  expected=res)
