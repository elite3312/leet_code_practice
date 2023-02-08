
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # get list len
        l = 0
        curr = head
        while True:
            if curr != None:
                l += 1
                curr = curr.next
            else: break
        if l == n:return head.next
        curr = head
        index = 0
        while True:
            if curr != None:
                index += 1

                if l-index == n:
                    temp = curr.next
                    curr.next = curr.next.next
                    del temp
                    break
                curr = curr.next
            else: break
        return head


if __name__ == "__main__":

    s = Solution()
    head = ListNode(1)  # [1, 2, 3, 4, 5]
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 4
    ans = s.removeNthFromEnd(head, n)
    print(ans)
    curr = ans
    while True:
            if curr != None:
                print(curr.val)
                curr = curr.next
            else :break
