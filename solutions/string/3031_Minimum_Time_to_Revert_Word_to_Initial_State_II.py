from utils.test_driver import test_driver

from cmath import sqrt
from collections import Counter
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        res=0
        remaining_right_chars=word
        
        while(1):
            res+=1
            if len(remaining_right_chars)>=k:
                remaining_right_chars=remaining_right_chars[k:]
            else:break
            if(word.startswith(remaining_right_chars)):break
        return res






        
if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                "abacaba",3
            ],
            # res
            2

        ],
       


    ]
    for input, res in tests:
        test_driver(s.minimumTimeToInitialState, input[0],input[1],  expected=res)
