class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Let dp(i, j) be the answer for inputs s1[:i] and s2[:j].
        dp = [
            [
            0 for j in range(len(s1)+1)
            ]
            for i in range(len(s2)+1)
            ]
        '''          s1 j
              x     s     e     a
            x null  s     se    sea
        s   e e     es    s     sa 
        2   a ea    ase   ...   ... 
        i   t eat   ...   ...   ...
        '''
        # init first rol and col
        for j in range(1, len(s1)+1):
            dp[0][j] = dp[0][j-1]+ord(s1[j-1])
            
        for i in range(1, len(s2)+1):
            dp[i][0] = dp[i-1][0]+ord(s2[i-1])
            
        
        # fill up table
        for i in range(1, len(s2)+1):
            for j in range(1, len(s1)+1):
                if s1[j-1]==s2[i-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+ord(s2[i-1]),
                                 dp[i][j-1]+ord(s1[j-1]))
        return dp[len(s2)][len(s1)]


def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.minimumDeleteSum(input1, input2)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)


if __name__ == "__main__":

    s = Solution()

    

    test_driver(s, "delete", "leet", 403)
    '''
    Deleting "dee" from "delete" to turn the string into "let",
    adds 100[d] + 101[e] + 101[e] to the sum.
    Deleting "e" from "leet" adds 101[e] to the sum.
    At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
    If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
    '''

    test_driver(s, 'sea', 'eat', 231)
    '''
    Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
    Deleting "t" from "eat" adds 116 to the sum.
    At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
    '''
