#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        curr=ListNode()
        head=curr
        while True:
            if list1==None or list2==None :
                break
            if list2.val<list1.val:
                _n=ListNode( list2.val)
                

                list2=list2.next
            else:
                _n=ListNode( list1.val)
                
                list1=list1.next
            
            curr.next=_n
            curr=curr.next
        if list1:
            while True:
                if list1==None:break
                _n=ListNode( list1.val)
                
                list1=list1.next
                curr.next=_n
                curr=curr.next
        else:
            
            while True:
                if list2==None:break
                _n=ListNode( list2.val)
                
                list2=list2.next
                curr.next=_n
                curr=curr.next
        return head.next

if __name__ == "__main__":
    sol=Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]

    print(sol.mergeTwoLists(list1,list2))
    