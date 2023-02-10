#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        n=0
        curr=head
        while True:
            if curr:
                n+=1
                curr=curr.next
            else:break
        if n==1:return None

        mid=n//2
        curr_index=0
        curr=head
        prev=None
        while True:
            if curr_index==mid:
                tmp=curr.next
                prev.next=tmp
                del curr
                break
            else:
                curr_index+=1
                prev=curr
                curr=curr.next
        return head
                
        
            


if __name__ == "__main__":
    pass