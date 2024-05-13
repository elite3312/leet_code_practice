
from utils.test_driver import test_driver

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        '''
        loop through each char in s, then find the same char in t and compute distance. Use a map to record visited chars in t.
        '''
        taken_from_t={}
        n=len(t)
        for i in range(n):
            taken_from_t[i]=False 
        m={}
        for i in range(n):
            for j in range(n):
                if taken_from_t[j]==False and t[j]==s[i]:
                    taken_from_t[j]=True
                    m[i]=abs(i-j)
        res=0
        for k in m:
            res+=m[k]
        return res
              


if __name__ == "__main__":
    sol = Solution()

    index = 0

    s = "abc"
    t = "bac"
    res = 2
    tests = [
        [#0
            [
            s,t
            ],
            res
        ],
        [#0
            [
             "abcde", "edbac"
            ],
            12
        ],

    ]

    for input, res in tests[index:]:
        test_driver(sol.findPermutationDifference, input[0],input[1], expected=res)
