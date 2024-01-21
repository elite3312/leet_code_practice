from utils.test_driver import test_driver

from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        if n<=8:return n
        c=Counter()

        for char in word:c[char]+=1

        l=[]
        for key in c:
            l.append(c[key])
        l.sort(reverse=True)#largest to smallest
        res=0

        key_count=0
        for val in l:
            if key_count<8:res+=val
            elif key_count<16:res+=val*2
            elif key_count<24:res+=val*3
            else:res+=val*4
            key_count+=1
        return res
    


        

        
if __name__ == "__main__":
    s = Solution()

    tests = [
        [  
                # inputs
                [
                   "amrvxnhsewkoipjyuclgtdbfq"
                ],
                # res
                52

            ],
            [  
                # inputs
                [
                   "abcde"
                ],
                # res
                5

            ],
            [ 
                # inputs
                [
                   "xycdefghij"
                ],
                # res
                12

            ],
            [  
                # inputs
                [
                   "cfjgleopq"
                ],
                # res
                10

            ],
           

    ]
    for input, res in tests:
        test_driver(s.minimumPushes, input[0], expected=res)
'''
idea
use counter to record char count

sort counter

if distinct chars <=8:then every char can be mapped to pushing once
if distinct chars <=16:then the first 8 chars with the largest count can be mapped to pushing once, the remining chars can be mapped to pushing twice.
and just repeat this logic
'''