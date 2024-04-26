from utils.test_driver import test_driver
'''
Hint 1
Use dynamic programming.
Hint 2
Let dp[i][j] be the answer for the first i rows such that column j is chosen from row i.
Hint 3
Use the concept of cumulative array to optimize the complexity of the solution.
'''
import heapq
class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)
        # Let dp[i][j] be the answer for the first i rows such that column j is chosen from row i.
        dp=[[None for _ in range(n)]for _ in range(n)]

        # base case for row 0
        for j in range(n):
            dp[0][j]=grid[0][j]

        for i in range(1,n):
            # use a heap to extract the first element in this row that has the minimum value and has a col that does not conflict with j
            heap=[]
            for index,val in  enumerate(dp[i-1]):
                heapq.heappush(heap,(val,index))
            for j in range(n):
                cur_heap=heap.copy()
                cur=heapq.heappop(cur_heap)#get the smallest entry
                while cur[1]==j:#while the col collides, get the next smallest entry
                    cur=heapq.heappop(cur_heap)

                dp[i][j]=cur[0]+grid[i][j]# the minimum from last row + grid[i][j]
        
        return min(dp[n-1])
        

if __name__ == "__main__":
    s = Solution()

    grid = [[1,2,3],[4,5,6],[7,8,9]]
    tests = [
        [
            # inputs
            [
               grid
            ],
            # res
            13
        ],
       
        
    ]
    for input, res in tests:
        test_driver(s.minFallingPathSum, input[0],   expected=res)