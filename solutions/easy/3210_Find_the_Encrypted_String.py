from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n=len(s)
        pos=k %(n)
        res=[]
        for i in range(pos,n):
            res.append(s[i])
        for i in range(pos):
            res.append(s[i])
        return "".join(res)
if __name__ == "__main__":
    sol = Solution()

    index =0

   
    tests=[
        [["dart",3],
        "tdar"],
        
    ]

    test_driver_main(sol.getEncryptedString, tests, index)
