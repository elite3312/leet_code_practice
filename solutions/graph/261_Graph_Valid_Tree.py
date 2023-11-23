from collections import defaultdict


class Solution:
    def validTree(self, n:int,edges: list[list[int]]) -> bool:
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited=[False for i in range(n)]

        def dfs(curr,pre):
            if visited[curr]:return False# found cycle

            visited[curr]=True
            for neighbor in graph[curr]:
                if neighbor!=pre:
                    if dfs(neighbor,curr) is False:return False
            return True
        return dfs(0,-1)

        

                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    out= True
    test_driver(s.validTree,n,edges,expected=out)

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    out= False
    test_driver(s.validTree,n,edges,expected=out)
    

# idea : check if nodes form connected graph w no cycle
# use visited hashmap to check cycles
# use pre to avoid going back