from collections import defaultdict,deque
from utils.test_driver import test_driver



class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        # Initialize a list to store the count of pairs for each distance
        res = [0] * n
        
        # Create an adjacency list for the houses and streets
        adjacency_list = defaultdict(list)
        for i in range(1, n):
            adjacency_list[i].append(i + 1)
            adjacency_list[i + 1].append(i)
        
        # Add the additional street connecting house x and house y
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)
        
        # Define a BFS function to find the minimum distance from a house
        def bfs(i):
            q = deque()
            visit = set()
            q.append((i, 0))
            visit.add(i)

            while q:
                i, dist = q.popleft()
                if dist > 0:
                    res[dist - 1] += 1
                for nei in adjacency_list[i]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, dist + 1))

        # Iterate through each house and perform BFS
        for i in range(1, n + 1):
            bfs(i)
        
        return res
        


if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                3, 1, 3
            ],
            # res
            [6, 0, 0]

        ],
        [
            # inputs
            [
                5,2,4
            ],
            # res
            [10,8,2, 0, 0]

        ],




    ]
    for input, res in tests:
        test_driver(s.countOfPairs, input[0], input[1], input[2], expected=res)
