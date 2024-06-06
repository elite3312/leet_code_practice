from utils.test_driver import test_driver
#from collections import deque
from collections import defaultdict
import heapq
class Solution:
    '''
    case 1
    1121*

    ->112

    case 2
    1121*3346*

    ->112346

    case 3
    abc*def*
    ->bcef

    '''
    def clearStars(self, s: str) -> str:
        # start from the left, main a dict to remember their pos, and find the smallest char. 
        # Stop when an asterisk is seen, 
        # and mark the index to delete.
        n=len(s)
        to_del=[False for _ in range(n)]

        #seen_star=False
        d=defaultdict(list)
        min_char=[]#heap
        for i in range(n):
            if s[i]!='*':
                d[s[i]].append(i)
                heapq.heappush(min_char,s[i])
            else:
                cur=heapq.heappop(min_char)
                  
                last=d[cur].pop(-1)
             
                
                to_del[last]=True
        res=[]
        for i in range(n):
            if not to_del[i] and s[i]!='*':res.append(s[i])
        return "".join(res)
                



        
if __name__ == "__main__":
    sol = Solution()

    index = 0


    tests = [
        [
            [
              "aaba*"
            ],
           "aab"
        ],
        [
            ["abc"]
            ,
           "abc"
        ],
        [
            ["abc*def*"]
            ,
           "cdef"
        ],
      
        
        
       
        
    ]

    fail_cnt=0
    for input, res in tests[index:]:
        if not test_driver(sol.clearStars, input[0], expected=res):
            fail_cnt+=1
    if fail_cnt>0:
        print("%d tests failed"%fail_cnt)

