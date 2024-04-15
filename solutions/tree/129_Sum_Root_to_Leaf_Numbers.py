from utils.test_driver import test_driver

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0

        def dfs(num: int, cur: TreeNode):
            if cur==None:return

            num *= 10
            num += cur.val
            if cur.left == None and cur.right == None: 
                nonlocal res
                res+= num
            dfs(num, cur.left)
            dfs(num, cur.right)
        dfs(0, root)
        return res


if __name__ == "__main__":
    s = Solution()

    tests = [

    ]
    for input, res in tests:
        test_driver(s.sumNumbers, input[0], input[1],  expected=res)
