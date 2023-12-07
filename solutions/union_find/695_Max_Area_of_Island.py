from utils.test_driver import test_driver

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        r=len(grid)
        c=len(grid[0])

        parent={}
        size={}

        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    parent[(i,j)]=(i,j)
                    size[(i,j)]=1
                else:
                    parent[(i,j)]=None
                    size[(i,j)]=0

        def valid_rc(i,j):
            return False if i<0 or j<0 or i>=r or j>=c else True
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        def find(x):
            if parent[x]==x:return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(a,b):
            a=find(a)
            b=find(b)
            if a!=b:
                if size[a]>=size[b]:
                    parent[b]=a
                    size[a]+=size[b]
                    size[b]=0
                else:
                    parent[a]=b
                    size[b]+=size[a]
                    size[a]=0
        
        has_one=False
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    has_one=True
                    for x,y in directions:
                        ni,nj=i+x,j+y
                        if valid_rc(ni,nj) and grid[ni][nj]:
                            union((i,j),(ni,nj))
        if has_one==False:return 0
        else :
            res=0
            for k,elem in size.items():
                res=max(res,elem)
            return res


    
        
if __name__ == "__main__":
    s=Solution()
    tests=[
        [[[0,0,1],
          [1,1,1]],4],
        [[[0,1,1],
          [1,1,0]],4],
        [[[1,1,1],
          [1,1,1]],6],
        [[[0,0,0],
          [0,0,1]],1],
        [[[0,0,0],
          [0,0,0]],0],
        [[[0,1,1],
          [0,0,1]],3],
        [[[0,0,1,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,1,1,0,1,0,0,0,0,0,0,0,0],
          [0,1,0,0,1,1,0,0,1,0,1,0,0],
          [0,1,0,0,1,1,0,0,1,1,1,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,0,0,0,0,0,0,1,1,0,0,0,0]],6],
        
    ]
    for a,b in tests:
        test_driver(s.maxAreaOfIsland,a,expected=b)