from utils.test_driver import test_driver
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        s_rev=s[::-1]
        n=len(s)
        for i in range(n-1):
            sub_two=s[i:i+2]
            if(sub_two in s_rev):return True
        return False


        
if __name__ == "__main__":
    s = Solution()
    
    tests = [
        [
            # inputs
            [
                 "leetcode"
            ],
            # res
             True

        ],
        [
            # inputs
            [
                 "abcba"
            ],
            # res
             True

        ],
        [
            # inputs
            [
                 "abcd"
            ],
            # res
             False

        ],
        
    ]
    for input, res in tests:
        test_driver(s.isSubstringPresent, input[0],  expected=res)
