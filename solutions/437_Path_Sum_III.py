# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.res = 0
        if not root:
            return 0
        if not root.left and not root.right:
            if targetSum == root.val:
                return 1
            else:
                return 0

        def inner(curr: TreeNode, sum: int, walked_path: list):

            if not curr:
                return
            sum += curr.val
            if sum == targetSum:
                self.res += 1
            
            tmp = sum
            #has_zero = False
            for elem in walked_path:
                #if elem == 0:
                    #has_zero = True
                tmp -= elem
                if tmp == targetSum:
                    #if has_zero:

                        #self.res += 1
                    self.res += 1
            new_walked_path = walked_path.copy()
            new_walked_path.append(curr.val)
            inner(curr.left, sum, new_walked_path)
            new_walked_path = walked_path.copy()
            new_walked_path.append(curr.val)
            inner(curr.right, sum, new_walked_path)
        inner(root, 0, [])
        return self.res


if __name__ == "__main__":
    #[0,1,1]
    #1 
    # expect4
    s = Solution()
    root = TreeNode()
    root.val =0
    c1 = TreeNode()
    c1.val = 1
    root.left = c1
    c2 = TreeNode()
    c2.val = 1
    
    root.right = c2
    ans = s.pathSum(root, 1)
    print(ans)
