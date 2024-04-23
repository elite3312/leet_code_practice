from utils.test_driver import test_driver
from collections import defaultdict,deque
# idea: repeatedly remove leafs until only 2 nodes remain
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]# only node is root
        
        # Initialize the adjacency list and degree of each node
        adjacency_list = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Initialize leaves queue
        leaves = deque([i for i in range(n) if degree[i] == 1])
        
        # Trim leaves until 2 or fewer nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in adjacency_list[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        
        return list(leaves)
            
 
if __name__ == "__main__":
    s = Solution()
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    Output= [3,4]
    tests = [
        [
            # inputs
            [
               n,edges
            ],
            # res
            Output
        ],
        
    ]
    for input, res in tests:
        test_driver(s.findMinHeightTrees, input[0],input[1],  expected=res)
