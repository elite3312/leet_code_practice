# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        if root==None:return []
        
        res=[]
        path=[]
        def inner(curr:TreeNode,curr_sum):
            if curr==None:return
            curr_sum+=curr.val
            path.append(curr.val)
            if curr_sum==targetSum and curr.left==None and curr.right==None:
                res.append(path.copy())
            else:
                inner(curr.left,curr_sum)
                inner(curr.right,curr_sum)
            path.pop(-1)
        inner(root,0)
        return res


if __name__ == "__main__":

    s = Solution()
    """
    target=22
    root = TreeNode(5)
    temp=TreeNode(4)
    root.left=temp
    temp=TreeNode(11)
    root.left.left=temp
    temp=TreeNode(7)
    root.left.left.left=temp
    temp=TreeNode(2)
    root.left.left.right=temp
    
    
    temp=TreeNode(8)
    root.right=temp
    temp=TreeNode(13)
    root.right.left=temp
    temp=TreeNode(4)
    root.right.right=temp
    
    temp=TreeNode(5)
    root.right.right.left=temp
    
    temp=TreeNode(1)
    root.right.right.right=temp"""
    target=0
    root = TreeNode(7)
    temp=TreeNode(0)
    root.left=temp
    temp=TreeNode(-1)
    root.left.left=temp
    temp=TreeNode(-6)
    root.left.right=temp
    temp=TreeNode(1)
    root.left.left.right=temp
    temp=TreeNode(-7)
    root.left.left.right.left=temp
    ans = s.pathSum(root,target)
    print(ans)
