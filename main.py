from utils.test_driver import test_driver

from collections import Counter
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        res=0
        
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
