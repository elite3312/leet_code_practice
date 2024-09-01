from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# import math
# import heapq


class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])# m, n is in [1,10]

        # mask是一個長度m的bit string，用以紀錄哪些row被選取了，長度最多10
        # prev是一個變數，紀錄上次拿得值，值從0到100
        # 我們要在二維陣列中從小的值取到大的值
        dp=[[-1 for j in range(101)]for i in range(1<<m)]# dp[i][j]=當狀態為mask，上一次取的值是j，達到的最大總和

        def dfs(mask,prev):
            if(mask == ((1<<m)-1)):# 11111..111, all rows visited，代表每個row都被拿過了
                return 0
            ret = dp[mask][prev]
            if(ret != -1):
                return ret
            ret = 0
            for i in range(m):
                if((mask>>i&1)==0):# if row i has not been visited
                    
                    for j in range(n):
                        if(grid[i][j] > prev):# 使用大於的條件即可保證所有取的值不重複
                            # ret=ret，代表不拿當前row，不繼續往下走
                            # ret=dfs(拿當前row的狀態,當前row的值)+grid[i][j]，代表拿當前row的值然後繼續往下
                            ret = max(ret, grid[i][j] + dfs( mask|(1<<i), grid[i][j]))
                
            dp[mask][prev]=ret
            return ret
        return dfs(0,0)
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[[[1,2,3],[4,3,2],[1,1,1]]], 8],
        [[[[8,7,6],[8,3,2]]],15]

    ]

    test_driver_main(sol.maxScore, tests, index)
