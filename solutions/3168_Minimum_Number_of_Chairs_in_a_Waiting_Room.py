#from collections import deque
from utils.test_driver import test_driver
class Solution:
    def minimumChairs(self, s: str) -> int:
        '''
        idea:
        maintain a cnter and monitor its max
        '''
        res=0
        max_res=-1
        for c in s:
            if c=='E':res+=1
            else:res-=1
            max_res=max(max_res,res)
        return max_res
if __name__ == "__main__":
    sol = Solution()

    index = 0


    tests = [
        [
            [
                "EEEEEEE"
            ],
            7
        ],
        [
            ["ELELEEL"]
            ,
            2
        ],
        [
            ["ELEELEELLL"]
            ,
            3
        ]
        
       
        
    ]

    fail_cnt=0
    for input, res in tests[index:]:
        if not test_driver(sol.minimumChairs, input[0], expected=res):
            fail_cnt+=1
    if fail_cnt>0:
        print("%d tests failed"%fail_cnt)

