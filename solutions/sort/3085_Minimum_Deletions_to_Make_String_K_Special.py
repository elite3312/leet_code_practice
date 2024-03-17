from utils.test_driver import test_driver
from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        #cnt
        cnt = Counter()
        for c in word:
            cnt[c] += 1
           
        # sort cnts
        freq = [cnt[k] for k in cnt]
        freq.sort()


        min_del = float('inf')
        for i in range(len(freq)):
            trgt = freq[i]#current center
            dels = 0#current delete sum
            for f in freq:
                #delete ones above upper bound
                if f>(trgt+k):
                    dels += f - (trgt+k)
                #delete ones below lower bound
                elif f < trgt:
                    dels += f
            min_del = min(min_del, dels)
            if min_del == 0:
                break
        
        return min_del if min_del != float('inf') else 0


if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                "aaabaaa", 2
            ],
            # res
            1

        ],
        [
            # inputs
            [
                "mummmu",  1
            ],
            # res
            1

        ],
        [
            # inputs
            [
                "dabdcbdcdcd",  2
            ],
            # res
            2

        ],
        [
            # inputs
            [
                "aabcaba", 0
            ],
            # res
            3

        ],

    ]
    for input, res in tests:
        test_driver(s.minimumDeletions, input[0], input[1],  expected=res)
