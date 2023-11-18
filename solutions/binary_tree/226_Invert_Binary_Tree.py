# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def post_order(node:TreeNode):
            if node is None:return

            post_order(node.left)
            post_order(node.right)
            _=node.left
            node.left=node.right
            node.right=_
        post_order(root)
        return root

                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()
    root=TreeNode(2)
    root.left=TreeNode(1)
    root.right=TreeNode(3)
    test_driver(s.invertTree,root,expected=None)
