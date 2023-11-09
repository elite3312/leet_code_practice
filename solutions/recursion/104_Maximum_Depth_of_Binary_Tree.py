# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:return 0
        self.max_depth=-1
        self.dfs(root,1)
        return self.max_depth
    def dfs(self,root:TreeNode,depth:int)->int:
        if root is None:return

        if root.left is None and root.right is None:
            if depth>self.max_depth:self.max_depth=depth
        self.dfs(root.left,depth+1)
        self.dfs(root.right,depth+1)

def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.maxDepth(input1)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)


if __name__ == "__main__":

    s = Solution()

