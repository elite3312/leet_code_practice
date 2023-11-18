# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root:TreeNode, k: int) -> int:
        res=[]
        def in_order(node):
            if node is None:return

            in_order(node.left)
            res.append(node.val)
            in_order(node.right)
        in_order(root)
        return res[k-1]
                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()
    root=TreeNode(2)
    root.left=TreeNode(1)
    root.right=TreeNode(3)
    test_driver(s.kthSmallest,root,1,expected=None)
