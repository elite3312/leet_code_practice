
from cmath import inf


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node, curMax):
            if not node:
                return
            if node.val >= curMax:
                count[0] += 1
                curMax = node.val
            dfs(node.left, curMax)
            dfs(node.right, curMax)
        
        count = [0]
        dfs(root, root.val)
        
        return count[0]
if __name__ == "__main__":
    s=Solution()
    '''
    #[3,3,null,4,2]
    root=TreeNode()
    root.val=3
    root.left=TreeNode()
    root.left.val=3
    
    root.left.left=TreeNode()
    root.left.left.val=4
    root.left.right=TreeNode()
    root.left.right.val=2
    s=Solution()
    print(s.goodNodes(root))'''
    
    #[3,1,4,3,null,1,5]
    root=TreeNode()
    root.val=3
    root.left=TreeNode()
    root.left.val=1
    root.right=TreeNode()
    root.right.val=4

    root.left.left=TreeNode()
    root.left.left.val=3

    root.right.left=TreeNode()
    root.right.left.val=1
    
    root.right.right=TreeNode()
    root.right.right.val=5
    print(s.goodNodes(root))