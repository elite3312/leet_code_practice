# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        '''
        The number of nodes in the tree is in the range [1, 1000].
        0 <= Node.val <= 1000
        '''
        w=h=1000
        Matrix = [[None for x in range(w)] for y in range(h)] 
        r=0
        c=0
        s=[]
        s.append(root)
        index=0
        while len(s):
            curr=s.pop[-1]
            #visit node
            if curr is not None:
                Matrix[r,c]=curr.val   
            index+=1
            
            s.append(curr.right)
            s.append(curr.left)
        pass
if __name__ == "__main__":
    s = Solution()
    root = [3,9,20,None,None,15,7]
    from utils import binary_tree_from_list
    root=binary_tree_from_list.to_binary_tree(root)
    print(s.verticalTraversal(root))
