# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:return [[root.val]]
        q=list()
        q.append(root)
        '''
          1
        2   3
           6 7
        '''
        res=[]
        
        while len(q)>0:
            # pop entire q and add elems.val to res[level]
            res.append([])# append a level
            curr_level_nodes=[]
            while len(q)>0:
                node=q.pop(0)
                res[-1].append(node.val)
                curr_level_nodes.append(node)


            # add all children to q
            for node in curr_level_nodes:
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return res
            



if __name__ == "__main__":
    s = Solution()
    '''
      1
    2   3
       6 7
    '''
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)

    root.right.left=TreeNode(6)
    root.right.right=TreeNode(7)

    print(s.levelOrder(root))

    '''
    [1,2,null,3,null,4,null,5]
        1
      2  x
    3  x
  4  x
5  
    '''
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.left.left=TreeNode(3)
    root.left.left.left=TreeNode(4)
    root.left.left.left.left=TreeNode(5)
    print(s.levelOrder(root))


