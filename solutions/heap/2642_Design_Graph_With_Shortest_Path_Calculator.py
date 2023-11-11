'''
There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

Implement the Graph class:

Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.
'''
import heapq
class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.adjlists=[[] for _ in range(n)]
 
        for edge in edges:
            self.adjlists[edge[0]].append((edge[1],edge[2]))

    def addEdge(self, edge: list[int]) -> None:

        self.adjlists[edge[0]].append((edge[1],edge[2]))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.adjlists)
        distances = [float('inf')] * n
        distances[node1] = 0

        # Priority queue to efficiently retrieve the node with the minimum distance
        priorityQueue = [(0, node1)]

        while priorityQueue:
            currentCost, currentNode = heapq.heappop(priorityQueue)

            # Skip if a shorter path has already been found
            if currentCost > distances[currentNode]:
                continue

            # If found the target node then return the cost
            if currentNode == node2:
                return currentCost

            # Explore neighbors and update distances
            for edge in self.adjlists[currentNode]:
                neighbor, edgeLength = edge
                newRouteCost = edgeLength + distances[currentNode]

                # Update distance if a shorter route is found
                if distances[neighbor] > newRouteCost:
                    distances[neighbor] = newRouteCost
                    heapq.heappush(priorityQueue, (newRouteCost, neighbor))
        return -1
def test_driver(s: Graph, *inputs, expected: str):
    # change this line
    ans = s.shortestPath(*inputs)

    for i in range(len(inputs)):
        print('input_%d : %s'%(i,str(inputs[i])))
    print("ans: ", ans)
    print('expected:', expected)
if __name__ == "__main__":
    n=4
    edges=[[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]
    s = Graph(n,edges)
    test_driver(s,3,2,expected=6)
    test_driver(s,0,3,expected=-1)
    s.addEdge([1, 3, 4])
    test_driver(s,0,3,expected=6)

    