from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque


class Solution:
    def getSmallestString(self, s: str) -> str:
        
        l=list(s)
        
        res="".join(l)

        n=len(s)
     
        for i in range(n-1):
            j =i+1
            if int(s[i])%2==int(s[j])%2:
                cur=l.copy()
                temp=cur[j]
                cur[j]=cur[i]
                cur[i]=temp

                cur_s="".join(cur)
        
                if int(cur_s)<=int(res):
                    res=cur_s
      
            
        return res
                
        
    
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[
            "45320"
        ],
            "43520"
        ],
        [[
            "82"
        ],
            "28"
        ],
        [[
            "10"
        ],
            "10"
        ],
        [[
            "13"
        ],
            "13"
        ],
        



    ]

    test_driver_main(sol.getSmallestString, tests, index)
