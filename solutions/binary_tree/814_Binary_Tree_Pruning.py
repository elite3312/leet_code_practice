# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root==None:return None
        if (root.val==0 and root.left==None and root.right==None):return None
        def inner(curr:TreeNode):
            if(curr == None):return 'empty'
            if curr.left!=None:
                if inner(curr.left)=='delete':curr.left=None
            if curr.right!=None:
                if inner(curr.right)=='delete':curr.right=None
            if(curr.val==0 and curr.left == None and curr.right == None ):return 'delete'
            else:return curr
                
           
        if inner(root)=='delete':return None
       
        return root
if __name__ == "__main__":
    
    s = Solution()
    from utils import binary_tree_from_list
    #root=binary_tree_from_list.to_binary_tree([1,None,0,None,None,0,1])
    root=binary_tree_from_list.to_binary_tree([0,None,0,None,None,0,0])
    #root=TreeNode(val=0)
    s.pruneTree(root)
    