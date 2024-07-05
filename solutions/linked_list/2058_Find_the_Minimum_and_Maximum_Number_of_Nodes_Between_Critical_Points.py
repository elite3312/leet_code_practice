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
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        cur=head
        prev=None
        prev_crit_index=-1
        left_most_crit_index=-1
        cur_index=0

        max_dist=-1
        min_dist=1e9
        while cur:
            # check for critical pt
            if cur_index>0 and cur.next !=None:
                if (prev.val < cur.val and cur.next.val<cur.val )or (prev.val > cur.val and cur.next.val>cur.val):
                    # check if there is a previous critical pt
                    if prev_crit_index!=-1:
                        cur_dist=cur_index-prev_crit_index
                        min_dist=min(cur_dist,min_dist)
                    if left_most_crit_index!=-1:
                        cur_dist=cur_index-left_most_crit_index
                        max_dist=cur_dist
                    if left_most_crit_index==-1:
                        left_most_crit_index=cur_index
                    # update 
                    prev_crit_index=cur_index
            prev=cur
            cur=cur.next
            cur_index+=1
        if min_dist==1e9:
            min_dist=-1
        return [min_dist,max_dist]
if __name__ == "__main__":
    sol = Solution()

    index =0

    # case 0
    t0= [5,3,1,2,5,1,2]
    head0=cur=ListNode(5)
    for elem in t0[1:]:
        cur.next=ListNode(elem)
        cur=cur.next
    
    # case 1
    t1= [5,9,1]
    head1=cur=ListNode(5)
    for elem in t1[1:]:
        cur.next=ListNode(elem)
        cur=cur.next
    tests=[
        [[head0],
        [1,3]],
        [[head1],
        [-1,-1]]
    ]

    test_driver_main(sol.nodesBetweenCriticalPoints, tests, index)
