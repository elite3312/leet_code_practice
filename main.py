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

        n = len(data)
        if n == 0:
            return None

        def inner(index: int = 0) -> TreeNode:
            """Closure function using recursion bo build tree"""
            if n <= index or data[index] is None:
                return None

            node = TreeNode(data[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node

        return inner()
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
    #print(inorderTraversal(root))

    a=ser.serialize(root)
    #print(a)
    b = deser.deserialize(a)
    print(inorderTraversal(b))

