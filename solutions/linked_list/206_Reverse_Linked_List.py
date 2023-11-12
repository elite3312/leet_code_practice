from utils.test_driver import test_driver
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) ->ListNode:
        if not head:return None
        curr=head
        prev=None
        while 1:
            if curr==None:break
            _=curr.next
            curr.next=prev
            prev=curr
            curr=_
        return prev
if __name__ == "__main__":
    s=Solution()
    #1->2->3->4->5
    #5->4->3->2->1
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next=ListNode(3)
    test_driver(s.reverseList,head,expected=None)
