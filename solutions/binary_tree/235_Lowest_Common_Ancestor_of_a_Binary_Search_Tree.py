# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        smaller,bigger=(p,q) if p.val<q.val else( q,p)

        res=None
        def inner(node:'TreeNode'):
            if node is None:return 0

            if smaller.val<=node.val and node.val<=bigger.val:
                nonlocal res
                res=node
                return  1
            elif smaller.val<node.val and bigger.val<node.val:
                if inner(node.left):return 1
            else:
                if inner(node.right):return 1
            return 0
        inner(root)
        return res



                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()
    root=TreeNode(2)
    root.left=TreeNode(1)
    root.right=TreeNode(3)
    test_driver(s.lowestCommonAncestor,root,root.left,root.right,expected=root)


    test_driver(s.lowestCommonAncestor,root,root,root.right,expected=root)
