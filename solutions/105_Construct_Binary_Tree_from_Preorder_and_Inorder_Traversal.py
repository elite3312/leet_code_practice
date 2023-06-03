# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution_0:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # in_index_map = dict(map(reversed, enumerate(inorder)))
        in_index_map = {val:key for key,val in enumerate(inorder)}
        def build_tree(pre_start: int, in_start: int, in_end: int) -> tuple[TreeNode | None, int]:
            if in_start >= in_end: return None, pre_start
            
            root_val = preorder[pre_start]
            root_index = in_index_map[root_val]
            
            l_tree, pre_end = build_tree(pre_start + 1, in_start, root_index)
            r_tree, pre_end = build_tree(pre_end, root_index + 1, in_end)
            
            return TreeNode(root_val, l_tree, r_tree), pre_end
        
        return build_tree(0, 0, len(inorder))[0]
class Solution:
    def buildTree(self, preorder:list, inorder:list):
        if inorder:
            INDEX = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[INDEX])
            root.left = self.buildTree(preorder, inorder[:INDEX])
            root.right = self.buildTree(preorder, inorder[INDEX+1:])
			
            return root

def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.buildTree(input1,input2)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)


if __name__ == "__main__":

    s = Solution()
    # pre, in
    test_driver(s,[3,9,20,15,7], [9,3,15,20,7],[3,9,20,None,None,15,7])

