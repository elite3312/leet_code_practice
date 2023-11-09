# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root) -> list[int]:
        res=[]
        def inner(curr):
            if curr is None:return 
            inner(curr.left)
            res.append(curr.val)
            inner(curr.right)
        inner(root)
        return res
        
if __name__ == "__main__":
    
    s = Solution()
    from utils import binary_tree_from_list
    #root=binary_tree_from_list.to_binary_tree([1,None,0,None,None,0,1])
    root=binary_tree_from_list.to_binary_tree([1,2,3,4,5,6,7,8,9,10,11,12,13])
    #root=TreeNode(val=0)
    ans=s.tree2str(root)
    print(ans)
    