from utils.test_driver import test_driver
'''
There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

Implement the Graph class:

Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.
'''
from collections import deque,defaultdict
class Graph:

    def __init__(self, routes: list[list[int]]):
      
        self.adjlists=defaultdict(set)
 
        for i,route in enumerate(routes):
            for stop in route:
                self.adjlists[stop].add(i)# i is the bus number
class Solution:    
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        # edge case 1
        if source==target:return 0
       
        s = Graph(routes)
        
        # bfs
        q=deque()
        first_routes=s.adjlists[source]
        visited=set()# keep track of visited bus routes
        for first_route in first_routes:  
            visited.add(first_route)
            q.append(first_route)# store routes
        busCount=1
        while q:
            curr_q_len=len(q)
            for i  in range(curr_q_len):
                curr_route=q.popleft()
                for stop in routes[curr_route]:
                    if stop==target:return busCount

                    for next_route in s.adjlists[stop]:
                        if next_route not in visited:
                            visited.add(next_route)
                            q.append(next_route)
            busCount+=1
        return -1
    

if __name__ == "__main__":
    s=Solution()
    routes = [[2],[2,8]]
    source = 2
    target = 8
    test_driver(s.numBusesToDestination,routes,source,target,expected=1)
    routes=[[1,2,7],[3,6,7]]
    source=1
    target=6
    test_driver(s.numBusesToDestination,routes,source,target,expected=2)
    routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    source = 15
    target = 12
    test_driver(s.numBusesToDestination,routes,source,target,expected=-1)

    '''
    Return 0 if the source and target are the same.

    Initialize an empty map from an integer to a list of integers adjList to store the edges. The key is the bus stop and the value is the list of integers denoting the indices of routes that have this stop.

    Initialize an empty queue q and an unordered set vis to keep track of visited routes.

    Insert the initial routes into the queue q and mark them visited in vis.

    Iterate over the queue while it's not empty and do the following:

    Pop the route from the queue.
    Iterate over the stops in the route.
    If the stop is equal to target, return busCount.
    Otherwise, iterate over the routes for this stop in the map adjList.
    Add the unvisited routes to the queue and mark them visited.
    Return -1 after completing the BFS.
    '''