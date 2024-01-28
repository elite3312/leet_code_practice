
from utils.test_driver import test_driver

class Solution:
    def countKeyChanges(self, s: str) -> int:
        last_key_lower='#'
        res=-1
        for c in s:
            c=str.lower(c)
            if c!=last_key_lower:res+=1
            last_key_lower=c
        return res
if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                "aAbBcC"
            ],
            # res
            2

        ],
        [
            # inputs
            [
                "aAAAAAAAAAaaaaaa"
            ],
            # res
            0

        ],
        




    ]
    for input, res in tests:
        test_driver(s.countKeyChanges, input[0],  expected=res)
# greedy