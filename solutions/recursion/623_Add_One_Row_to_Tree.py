from utils.test_driver import test_driver

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth==1:
            cur=TreeNode(val)
            cur.left=root
            return cur
        target_depth=depth-1
        res=[]
        def reach_certain_depth(cur: TreeNode,depth:int):
            nonlocal target_depth
            if cur==None:return
            reach_certain_depth(cur.left,depth+1)
            reach_certain_depth(cur.right,depth+1)
            if depth==target_depth:res.append(cur)
        reach_certain_depth(root,1)

        for node in res:
            cur=TreeNode(val)
            cur.left=node.left
            node.left=cur

            cur=TreeNode(val)
            cur.right=node.right
            node.right=cur
        return root
if __name__ == "__main__":
    s = Solution()

    root=TreeNode(0)
    root.left=TreeNode(1)
    root.right=TreeNode(2)
    
    root.left.left=TreeNode(3)
    root.left.right=TreeNode(4)

    root.left.left.left=TreeNode(5)
    val=10
    tests = [
        [[root,val,3],root]
    ]
    for input, res in tests:
        test_driver(s.addOneRow, input[0], input[1],input[2] , expected=res)
