from functools import lru_cache


class Solution:  # 36 ms, faster than 34.07%
    def numDecodings(self, s: str) -> int:

        @lru_cache(None)
        def dp(i):
            if i == len(s): return 1
            ans = 0
            if s[i] != '0':  # Single digit
                ans += dp(i + 1)
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] <= '6'):  # Two digits
                ans += dp(i + 2)
            return ans

        return dp(0)

def test_driver(s: Solution, input1: any, input2: any, expected: str):
    ans = s.numDecodings(input1)
    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)


if __name__ == "__main__":

    s = Solution()

    input1 = "12"
    expected = 2
    test_driver(s, input1, None, expected)

    input1 = "226"
    expected = 3
    test_driver(s, input1, None, expected)

    input1 = "06"
    expected = 0
    test_driver(s, input1, None, expected)

    input1 = "106"
    expected = 1
    test_driver(s, input1, None, expected)