from utils.test_driver import test_driver_main
from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        hold=head
        cur=head.next
        _sum=0
        while cur:
            if cur.val==0:
                hold.val=_sum
                _sum=0
                if cur.next==None:
                    hold.next=None
                    break
                else:    
                    hold.next=cur
                    hold=cur
            else:
                _sum+=cur.val
            cur=cur.next
        return head
if __name__ == "__main__":
    sol = Solution()

    index =0

    t0=[0,3,1,0,4,5,2,0]
    cur=ListNode(0)
    head0=cur
    for elem in t0[1:]:
        cur.next=ListNode(elem)
        cur=cur.next
    tests=[
        [[head0],
        head0]
    ]

    test_driver_main(sol.mergeNodes, tests, index)
