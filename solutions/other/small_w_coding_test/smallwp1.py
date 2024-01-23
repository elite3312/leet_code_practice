from utils.test_driver import test_driver

class Solution:
    def number_of_unchanged_char_after_reverse(self,s):
        res = 0
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        j = n-1
        for i in range(n//2):
            if s[i] == s[j]:
                res += 1
            j -= 1
        if n % 2 == 0:
            res *= 2
        else:
            res = res*2+1
        return res


                    
        

if __name__ == "__main__":
    s = Solution()
 

    tests = [
            [#case 1
            # input
            [
                "alphxxdida"
            ],
            #res
            4
            ],[#case 2
            # input
            [
                "alp"
            ],
            #res
            1
            ],
            [#case 3
            # input
            [
                "alaha"
            ],
            #res
            3
            ],
        ]
    for input, res in tests:
        test_driver(s.number_of_unchanged_char_after_reverse, input[0], expected=res)
