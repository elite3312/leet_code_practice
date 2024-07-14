from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        rowCnt,colCnt,res=1,1,0

        i=(m-1)-1
        j=(n-1)-1
        while i>=0 and j>=0:
            if horizontalCut[i]>verticalCut[j]:
                res+=horizontalCut[i]*colCnt
                rowCnt+=1
                i-=1
            else:
                res+=verticalCut[j]*rowCnt
                colCnt+=1
                j-=1
        if i>=0:
            while i >= 0 :
                res += horizontalCut[i] * colCnt
                rowCnt+=1
                i-=1
        else:
            while j >= 0 :
                res += verticalCut[j] * rowCnt
                colCnt+=1
                j-=1
        
        return res

if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[1,7,[],[2,1,2,1,2,1]],9],
        [[3,2,[1,3],[5]],13],
        [[2,2,[7],[4]],15],
        [[1,1,[],[]],0]



    ]

    test_driver_main(sol.minimumCost, tests, index)
