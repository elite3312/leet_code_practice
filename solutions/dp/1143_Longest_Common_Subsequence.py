from collections import defaultdict,deque
from utils.test_driver import test_driver



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n_1,n_2=len(text1),len(text2)
        dp=[[0 for _ in range(n_2+1)]for _ in range(n_1+1)]#dp[i][j]=len of lcs  for text1[:i] and text[2][:j]

        for i in range(1,n_1+1):
            for j in range(1,n_2+1):
                if text1[i-1]==text2[j-1]:dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n_1][n_2]

        


if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                "abcde","ace"
            ],
            # res
         3

        ],
       

    ]
    for input, res in tests:
        test_driver(s.longestCommonSubsequence, input[0], input[1],  expected=res)
'''
In mathematics, a subsequence of a given sequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements. 

use dp
'''