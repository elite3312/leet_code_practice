from utils.test_driver import test_driver
from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        res=0
        for i in range (n):
            for j in range(i,n):
                is_valid=True
                cnter=Counter()
                for c in s[i:j+1]:
                    cnter[c]+=1
                    if cnter[c]>=3:
                        is_valid=False
                        break
                
                if is_valid:
                    res=max(res,j-i+1)
        return res

if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                "bcbbbcba"
            ],
            # res
            4

        ],
       

    ]
    for input, res in tests:
        test_driver(s.maximumLengthSubstring, input[0],  expected=res)
