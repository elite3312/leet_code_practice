from utils.test_driver import test_driver_main
#import functools
# from utils.linked_list import print_list
#from itertools import combinations
# from collections import Counter
# from collections import deque
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]# dp[i][j]:  the minimum prints to print s[i:j+1]

        def inner(i: int, j: int) -> int:
            #end condition
            if i > j:
                return 0
            elif i==j:
                return 1

            #end condition
            if dp[i][j] != -1:
                return dp[i][j]

            first_letter = s[i]
            # If the current character is not repeated in the rest of the string
            answer = 1 + inner(i + 1, j) # at
            for k in range(i + 1, j + 1):
                # If repeated then update the answer
                if s[k] == first_letter:
                    # Splitting from i -> k - 1 (remove the same character)
                    # and from k + 1 -> j             
                    maybe_better_answer = inner(i, k - 1) + inner(k + 1, j)
                    answer = min(answer, maybe_better_answer)
            dp[i][j]=answer
            return answer
        return inner(0, n - 1)
if __name__ == "__main__":

    sol = Solution()

    index = 0

    tests = [
        [["aaabbb"],2],
        [
          ["aba"]  ,2
        ],
    ]

    test_driver_main(sol.strangePrinter, tests, index)
