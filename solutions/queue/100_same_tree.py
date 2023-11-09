# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q:TreeNode) -> bool:
        queue_p=[]
        queue_q=[]
        queue_p.append(p)
        queue_q.append(q)

        while len(queue_p)>0 and len(queue_q)>0:
            #pop
            p_node=queue_p.pop(0)
            q_node=queue_q.pop(0)

            if p_node == None and q_node==None:
                pass
            elif  p_node == None or q_node == None:
                return False
            else:
                if p_node.val !=  q_node.val:
                    return False
                else:
                    queue_p.append(p_node.left)
                    queue_p.append(p_node.right)
                    queue_q.append(q_node.left)
                    queue_q.append(q_node.right)
        return True

def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.isSameTree(input1,input2)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)


if __name__ == "__main__":

    s = Solution()

    p1=TreeNode()
    p1.left=TreeNode(val=1)

    p2=TreeNode()
    p2.left=TreeNode(val=1)
    test_driver(s,p1,p2,True)

