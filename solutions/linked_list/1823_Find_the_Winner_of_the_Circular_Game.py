from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque

class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k==1:
            return n
        head:ListNode=ListNode()
        cur:ListNode=head
        for i in range(n):
            new_node=ListNode(i)
            cur.next=new_node
            cur=cur.next

            if i==n-1:
                cur.next=head.next

        cur=head.next
        rem=n
        while rem:
            for i in range(k-1):
                prev=cur
                cur=cur.next
            
            # del
            prev.next=cur.next
            del cur
            cur=prev.next
            rem-=1
            
        return cur.val+1
            


if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[5,2],
         3
         ],
         [[6,5],
         1
         ],
         [[3,1],
         26
         ],
      
    ]

    test_driver_main(sol.findTheWinner, tests, index)
