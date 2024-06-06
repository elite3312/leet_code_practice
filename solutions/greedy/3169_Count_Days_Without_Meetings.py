#from collections import deque
from utils.test_driver import test_driver
class Solution:
   
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        merged_intervals =[]
        for interval in meetings:
            # if the merged_intervals is empty or if the current interval is not overlapped with the rightmost merged interval
            # then we create a new entry
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            # otherwise with simply merge
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        res=days

        for m in merged_intervals:
            res-=m[1]-m[0]+1
        return res



        
if __name__ == "__main__":
    sol = Solution()

    index = 0


    tests = [
        [
            [
               10,[[5,7],[1,3],[9,10]]
            ],
            2
        ],
        [
            [5, [[2,4],[1,3]]]
            ,
            1
        ],
        [
            [6,[[1,6]]]
            ,
            0
        ]
        
       
        
    ]

    fail_cnt=0
    for input, res in tests[index:]:
        if not test_driver(sol.countDays, input[0],input[1], expected=res):
            fail_cnt+=1
    if fail_cnt>0:
        print("%d tests failed"%fail_cnt)

