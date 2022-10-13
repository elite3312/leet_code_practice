#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node:ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        parent_next=node
        tmp=node.next
        del node
        parent_next=tmp
        
            


if __name__ == "__main__":
    pass