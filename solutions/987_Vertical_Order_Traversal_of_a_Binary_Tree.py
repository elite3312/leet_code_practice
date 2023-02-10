from utils import binary_tree_from_list
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
        d={}#dict that hashes (r,c)to a node
        def inner(curr:TreeNode,r,c):
            if curr is None:return
            inner(curr.left,r+1,c-1)
            inner(curr.right,r+1,c+1)
            if (r,c) not in d.keys():
                d[r,c]=[]
            
            d[r,c].append(curr.val)
            d[r,c].sort()
        inner(root,0,0)
        res=[]
        
        r=[]
        c=[]
        
        for k in d.keys():
            if k[0]not in r:r.append(k[0])
            if k[1]not in c:c.append(k[1])
        r.sort()
        c.sort()
        #print(d.keys())
        #print(r)
        #print(c)
       
        for col in c:
            temp_list=[]
            for row in r: 
                try:
                #if (row,col) in d.keys():
                    for elem in d[(row,col)]:
                        temp_list.append(elem)
                except:pass
            if len(temp_list)>0:
                res.append(temp_list)
        return res
        
if __name__ == "__main__":
    s = Solution()
    #root = [3,9,20,None,None,15,7]
    root=[1,2,3,4,6,5,7]
    #root=[0,None,1,2]
    
    root=binary_tree_from_list.to_binary_tree(root)
    print(s.verticalTraversal(root))
