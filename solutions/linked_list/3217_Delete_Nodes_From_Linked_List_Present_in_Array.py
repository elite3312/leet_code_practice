from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        _set=set(nums)
        new_head=ListNode(-1)
        new_cur=new_head

        cur=head
        while cur:
            if cur.val not in _set:
                _new_node=ListNode(cur.val)
                new_cur.next=_new_node
                new_cur=_new_node
            cur=cur.next
        return new_head.next
                
        
    
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        



    ]

    test_driver_main(sol.modifiedList, tests, index)
