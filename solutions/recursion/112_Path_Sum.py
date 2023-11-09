#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root:TreeNode, targetSum: int) -> bool:
        self.res=False
        def inner(curr:TreeNode,targetSum:int):
            if not curr:return
            if not curr.left and not curr.right and targetSum==curr.val:
                self.res=True
            inner(curr.left,targetSum-curr.val)
            inner(curr.right,targetSum-curr.val)
        inner(root,targetSum)
        return self.res
        
if __name__ == "__main__":

    s = Solution()
    root=TreeNode()
    root.val=5
    c1=TreeNode()
    c1.val=4
    root.left=c1
    ans = s.hasPathSum(root,9)
    print(ans)
