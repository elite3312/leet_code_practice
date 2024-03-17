from utils.test_driver import test_driver
'''
    abada
+1  _
+2  ___
+3  _____
'''
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        res=0
        n=len(s)
        prev_c_occurences=0
        for i in range (n):
            if s[i]==c:
                res+=1+prev_c_occurences
                prev_c_occurences+=1
        return res
    def countSubstrings_tle(self, s: str, c: str) -> int:
        res=0
        n=len(s)
        for i in range (n):
            for j in range (i,n):
                if s[i]==c and c==s[j]:
                    res+=1
        return res

        
if __name__ == "__main__":
    s = Solution()
    
    tests = [
        [
            # inputs
            [
                 "abada","a"
            ],
            # res
             6

        ],
        [
            # inputs
            [
                 "zzz","z"
            ],
            # res
             6

        ],        
    ]
    for input, res in tests:
        test_driver(s.countSubstrings, input[0], input[1],  expected=res)
