from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque

class Solution:
    def minOperations(self, logs: list[str]) -> int:
        depth=0
        for log in logs:
            if log=='./':
                pass
            elif log=='../':
                if depth>0:
                    depth-=1
            else:
                depth+=1
        return depth

if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[
            ["d1/","d2/","../","d21/","./"]
        ],
           2
        ],
        [[
            ["d1/","d2/","./","d3/","../","d31/"]
        ],
           3
        ],
        [[
            ["d1/","../","../","../"]
        ],
           0
        ],
        

    ]

    test_driver_main(sol.minOperations, tests, index)
