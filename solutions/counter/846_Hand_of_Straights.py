from utils.test_driver import test_driver
from utils.text_colors import bcolors
'''
built-in libraries imports
'''
from collections import Counter
#from collections import deque
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # init and edge case check
        n=len(hand)
        if n%groupSize!=0:return False

        # use a cnter to remeber occurences of numbers
        d=Counter()
        min_e=1e9+1
        max_e=-1e9
        for e in hand:
            d[e]+=1
            min_e=min(min_e,e)
            max_e=max(max_e,e)
        cur=min_e

        processed_elem_cnt=0
        while 1:
            # search for a consecutive hand
            break_flag=False
            for i in range(groupSize):
                if d[cur+i]==0:
                    break_flag=True
                    break
                else:
                    d[cur+i]-=1
                    processed_elem_cnt+=1
            if break_flag:break

            # update cur to point to a non-zero entry
            break_flag=False
            while d[cur]==0:
                if cur<=max_e:
                    cur+=1
                else:
                    break_flag=True
                    break
            if break_flag:break
        #check if we did in fact see n numbers in consecutive hands
        if processed_elem_cnt!=n:return False
        else: return True

        
if __name__ == "__main__":
    sol = Solution()

    index = 0


    tests = [
        [
            [
                [10,12,8],3
            ],
            False
        ],
        [
            [
                [1,2,3,6,2,3,4,7,8],3
            ],
            True
        ],
        [
            [
                [1,2,3,4,5],4]
            ,
            False
        ]
        
       
        
    ]

    fail_cnt=0
    for input, res in tests[index:]:
        if not test_driver(sol.isNStraightHand, input[0],input[1], expected=res):
            fail_cnt+=1
    if fail_cnt>0:
        print(bcolors.FAIL+"%d tests failed"%fail_cnt+bcolors.ENDC)
    else:
        print(bcolors.OKGREEN+"All %s tests passed"%len(tests)+bcolors.ENDC)
