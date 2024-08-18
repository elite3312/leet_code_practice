from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
#from itertools import combinations
# from collections import Counter
# from collections import deque
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n=len(s)
        res=0
        for i in range (1,n+1):
            for j in range(n):
                if j+i>n:
                    break
                print(s[j:j+i])
                ones,zeroes=0,0
                violated=False
                for a in range(j,j+i):
                    if s[a]=='1':
                        ones+=1
                    else:
                        zeroes+=1
                    if ones>k and zeroes>k:
                        violated=True
                        break
                if not violated:
                    res+=1
        return res
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [
          ["10101",1]  ,12
        ]
    ]

    test_driver_main(sol.countKConstraintSubstrings, tests, index)
