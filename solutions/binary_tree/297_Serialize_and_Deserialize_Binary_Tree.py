from utils.test_driver import test_driver
from utils.traverse import inorderTraversal
import pickle,base64
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:

    def serialize(self, root)->str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=[]
        q=deque()
        q.append(root)
        while len(q)>0:
            cur=q.popleft()
            if cur is None:
                res.append(None)
            else:
                res.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
        res_str=pickle.dumps(res)
        res_str=base64.b64encode(res_str)
        res_str=str(res_str,'utf-8')
        return res_str

    def deserialize(self,data: str) -> TreeNode:
        """Create BT from list of values."""
        data=base64.b64decode(data)
        data=pickle.loads(data)

        # remove trailinig nones
        for i in range(len(data)):
            if data[-(i+1)]!=None:
                break
        data=data[:-(i+1)+1]

        n = len(data)
        if n == 0:
            return None

        q=[]
        root=TreeNode(data[0])
        q.append(root)
        i=0
        while len(q)>0:
            node=q.pop(0)
            i=i+1
            if i>=n:break
            if(data[i]==None):
                node.left=None
            else:
                node.left=TreeNode(data[i])
                q.append(node.left)
            i=i+1
            if i>=n:break
            if(data[i]==None):
                node.right=None
            else:
                node.right=TreeNode(data[i])
                q.append(node.right)
        return root
            


if __name__ == "__main__":
    ser = Codec()
    deser = Codec()
    # 123xx4567
    '''
        1
       2 3
      x x 4 5
         6 7
    '''
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.right.left=TreeNode(4)
    root.right.right=TreeNode(5)
    root.right.left.left=TreeNode(6)
    root.right.left.right=TreeNode(7)
    print(inorderTraversal(root))

    a=ser.serialize(root)
    b = deser.deserialize(a)
    print(inorderTraversal(b))

    # 123xx45
    '''
        1
       2 3
      x x 4 5
    '''
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.right.left=TreeNode(4)
    root.right.right=TreeNode(5)
    print(inorderTraversal(root))
    a=ser.serialize(root)
    b = deser.deserialize(a)
    print(inorderTraversal(b))