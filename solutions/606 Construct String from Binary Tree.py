# Definition for a binary tree node.
from sre_constants import AT_END_STRING
import string


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root:TreeNode) -> str:
        def inner(curr:TreeNode):
            if curr==None:return None
            
            left=inner(curr.left)
            right=inner(curr.right)
            if left==right==None:
                return str(curr.val)
            elif left==None and right!=None:
                
                return str(curr.val)+'()'+'('+right+')'
            elif left!=None and right==None:
                return str(curr.val)+'('+left+')'
            else:
                return str(curr.val)+'('+left+')'+'('+right+')'
            
 
        return inner(root)
if __name__ == "__main__":
    
    s = Solution()
    from utils import binary_tree_from_list
    #root=binary_tree_from_list.to_binary_tree([1,None,0,None,None,0,1])
    root=binary_tree_from_list.to_binary_tree([1,2,3,4,5,6,7,8,9,10,11,12,13])
    #root=TreeNode(val=0)
    ans=s.tree2str(root)
    print(ans)
    