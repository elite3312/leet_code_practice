from utils.test_driver import test_driver
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited=[[0 for c in range(len(grid[0]))]for r in range(len(grid))]
        def dfs(r,c):
            if not valid_rc(r,c):return 
            if visited[r][c]:return 
            if grid[r][c]=='0':return 
            visited[r][c]=1
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
       
        def valid_rc(r,c):
            if r <0 or r>=len(grid):return 0
            if c<0 or c>=len(grid[0]):return 0
            return 1
        res=0
        for r in range(len(grid)):
            for c in  range(len(grid[0])):
                if grid[r][c]=='1' and not visited[r][c]:
                    res+=1
                    dfs(r,c)
        return res
if __name__ == "__main__":
    s=Solution()
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    ans=1
    test_driver(s.numIslands,grid,expected=ans)

    grid =[
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    ans=3
    test_driver(s.numIslands,grid,expected=ans)
