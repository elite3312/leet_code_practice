from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        # dp[i]=True iff s[i+1:n] can be segmented by the wordDict
        @lru_cache(None)
        def dp(start):
            if start == n:  # Found a valid way to break words
                return True

            for end in range(start + 1, n + 1):  # O(N^2)
                word = s[start:end]  # O(N)
                if word in wordSet and dp(end):
                    return True
            return False

        return dp(0)
def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.wordBreak(input1,input2)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)



if __name__ == "__main__":

    s = Solution()
    test_driver(s,'leet',["leet",'code'],True)
    test_driver(s,'leetcode',["leet","code"],True)
    test_driver(s,'applepenapple',["apple","pen"],True)
    test_driver(s,'catsandog',["cats","dog","sand","and","cat"],False)

    test_driver(s,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
                ,["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"],False)
    
