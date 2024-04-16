from utils.test_driver import test_driver

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        def reach_certain_depth(root: TreeNode,depth:int):
            cur_depth=0
            q=[]
            q.append(root)
            while len(q):
                cur_depth+=1

if __name__ == "__main__":
    s = Solution()

    tests = [

    ]
    for input, res in tests:
        test_driver(s.sumNumbers, input[0], input[1],  expected=res)
