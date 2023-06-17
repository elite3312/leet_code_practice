
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldtonew = {}# maps old nodes to new nodes
        return self.dfs(node, oldtonew)

    def dfs(self, node, oldtonew):
        if not node:
            return None
        if node in oldtonew:
            return oldtonew[node]
        copy = Node(node.val)
        oldtonew[node] = copy# map old node to copied node
        for n in node.neighbors:
            copy.neighbors.append(self.dfs(n, oldtonew))
        return copy

def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.cloneGraph(input1)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)



if __name__ == "__main__":

    s = Solution()
    
    
