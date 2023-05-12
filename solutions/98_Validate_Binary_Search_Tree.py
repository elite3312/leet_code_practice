# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        path=[]
        self.in_order_traverse(root,path)

        for i in range(len(path)-1):
            if path[i]>=path[i+1]:return False
        return True
    def in_order_traverse(self,root:TreeNode,path:list):
        if root is None:
            return 
        self.in_order_traverse(root.left,path)
        path.append(root.val)
        self.in_order_traverse(root.right,path)

def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.numDecodings(input1)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)


if __name__ == "__main__":

    s = Solution()

