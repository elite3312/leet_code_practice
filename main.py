#from collections import deque
from utils.test_driver import test_driver
from utils.text_colors import bcolors
class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        n=len(nums1)
        m=len(nums2)
        res=0
        for i in range (n):
            for j in range (m):
                if nums1[i]%(nums2[j]*k)==0:
                    res+=1
        return res
if __name__ == "__main__":
    sol = Solution()

    index = 0


    tests = [
        [
            [
                [1,3,4],[1,3,4],1
            ],
            5
        ],
        [
            [[1,2,4,12],[2,4],3]
            ,
            2
        ]
        
       
        
    ]

    fail_cnt=0
    for input, res in tests[index:]:
        if not test_driver(sol.numberOfPairs, input[0],input[1],input[2], expected=res):
            fail_cnt+=1
    if fail_cnt>0:
        print(bcolors.FAIL+"%d tests failed"%fail_cnt+bcolors.ENDC)
    else:
        print(bcolors.OKGREEN+"All %s tests passed"%len(tests)+bcolors.ENDC)
