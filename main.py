
from cmath import inf


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        unvisited=[]
        unvisited.append(root)
        max_left=-inf
        on='_'
        max_right=-inf
        good_nodes=0
        while len(unvisited)!=0:
            curr=unvisited.pop()
            if curr==root:
                good_nodes+=1
            if curr.left:
                if curr==root:
                    on='left'
                unvisited.append(curr.left)
                if curr!=root:
                    match on:
                        case 'left':
                            if max_left<=curr.val:good_nodes+=1
                            max_left=max(max_left,curr.val)
                        case 'right':
                            if max_right<=curr.val:good_nodes+=1
                            max_right=max(max_right,curr.val)
                        case _:pass   
            if curr.right:
                
                if curr==root:
                    on='right'
                unvisited.append(curr.right)
                if curr!=root:
                    match on:
                        case 'left':
                            if max_left<=curr.val:good_nodes+=1
                            max_left=max(max_left,curr.val)
                        case 'right':
                            if max_right<=curr.val:good_nodes+=1
                            max_right=max(max_right,curr.val)
                        case _:pass   
        
        return good_nodes
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