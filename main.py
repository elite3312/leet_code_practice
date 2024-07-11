from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque

class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        rev=[]
        res=[]
        left_brac_cnt=0

        stop_i=None
        for i,c in enumerate(s):
            if c == '(':
                left_brac_cnt+=1
            elif c==')':
                if not stop_i:
                    stop_i=i
            else:
                res.append(c)
                if stop_i:
                    rev.append(False)
                else:
                    if left_brac_cnt%2==1:
                        rev.append(True)
                    else:
                        rev.append(False)
        n=len(res)
        swapped=[False for i in range(n)]
        for i in range(n):
            if rev[i] and not swapped[i]:
                temp=res[-(i+1)]
                res[-(i+1)]=res[i]
                res[i]=temp
                swapped[-(i+1)]=True
        
        return ''.join(res)
if __name__ == "__main__":
    sol = Solution()

    index = 1

    tests = [
        [[
           "(abcd)"
        ],
           "dcba"
        ],
        [[
           "(ed(et(oc))el)"
        ],
           "leetcode"
        ],
       
        

    ]

    test_driver_main(sol.reverseParentheses, tests, index)
