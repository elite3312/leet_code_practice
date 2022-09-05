
# Definition for a Node.

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> list[list[int]]:
        if root is None:return []
        q=[]
        level=0
        q.append((root,level))
        ans=[]
        while len(q):
            curr=q.pop(0)

            if len(ans)<curr[1]+1:
                ans.append([])
            ans[curr[1]].append(curr[0].val)

            for c in curr[0].children:
                q.append((c,curr[1]+1))
        return ans
            
if __name__ == "__main__":
    s = Solution()
    #root = [3,9,20,None,None,15,7]
    root=[1,2,3,4,6,5,7]
    #root=[0,None,1,2]
    
    root=binary_tree_from_list.to_binary_tree(root)
    print(s.verticalTraversal(root))
