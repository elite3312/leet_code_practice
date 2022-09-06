# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def inner(curr:TreeNode):
            if(curr == None):return
            inner(curr.left)
            inner(curr.right)
            if(curr.val==0 and curr.left == None and curr.right == None ):
                curr=None
           
        inner(root)
        return root
if __name__ == "__main__":
    '''
    s = Solution()
    from utils import binary_tree_from_list
    #root=binary_tree_from_list.to_binary_tree([1,None,0,None,None,0,1])
    root=TreeNode(val=0)
    s.pruneTree(root)
    pass'''

    root=TreeNode(val=0)
    print(id(root))
    def debug(curr:TreeNode):
        print(id(curr))
        curr=None
        print(id(curr))
    debug(root)
    print(id(root))
    root=None
    
    print(id(root))