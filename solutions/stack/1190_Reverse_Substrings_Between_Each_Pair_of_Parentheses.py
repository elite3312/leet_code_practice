from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        

        brak_pairs = []
        closed_braks=[]
        char_cnt=0
        for i, c in enumerate(s):
            if c == '(':
                brak_pairs.append([i, None])
            elif c == ')':
                brak_pairs[-1][1] = i
                closed_braks.append(brak_pairs.pop(-1))
                
            else:
                char_cnt+=1
        if char_cnt==0:return ''
        brak_len = len(closed_braks)
        if brak_len==0:
            return s
        
        # outer=[3000,3000]
# 
        # outer_braks=[]
        # inner_braks=[]
        # for i in range(brak_len-1,-1,-1):
        #     if closed_braks[i][0]<outer[0] and closed_braks[i][1]<outer[1] :
        #         outer=closed_braks[i]
        #         outer_braks.append(outer)
        #         inner_braks.append([])
        #     else:
        #         inner_braks[-1].append(closed_braks[i])
        
        res=list(s)
        for o in closed_braks:
            if o[1]-o[0]==1:continue
            left,right=o[0]+1,o[1]-1
            temp=[c for c in res[left:right+1] if c not in ['(',')']]
            k=0
            for i in range(left,right+1):
                if res[i] not in ['(',')']:
                    res[i]=temp[-1-k]
                    k+=1

        res=[c for c in res if c not in ['(',')']]
        return ''.join(res)
        
    
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[
            "ta(aaz(xx()y))usw((((a))))"
        ],
            "taxxyzaauswa"
        ],
         [[
            "ta()usw((((a))))"
        ],
            "tauswa"
        ],
         [[
            "(())"
        ],
            ""
        ],
        [[
            "x"
        ],
            "x"
        ],
        [[
            "(abcd)"
        ],
            "dcba"
        ],
        [[
            "(u(love)i)"
        ],
            "iloveu"
        ],
        [[
            "(ed(et(oc))el)"
        ],
            "leetcode"
        ],
        [[
            "a(bcdefghijkl(mno)p)q"
        ],
            "apmnolkjihgfedcbq"
        ],



    ]

    test_driver_main(sol.reverseParentheses, tests, index)
