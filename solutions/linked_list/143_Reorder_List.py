# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 1. check edge cases
        if head.next==None:return
        if head.next.next==None:return

        # 2. create array to store references of nodes
        l=list()
        curr=head
        while curr:
            l.append(curr)
            curr=curr.next
        
        # reorder
        ptr1=1
        ptr2=len(l)-1
        curr=head
        while 1:
            curr.next=l[ptr2]
            curr=curr.next
            ptr2-=1
            if ptr2<=ptr1:
                curr.next=l[ptr1]
                curr=curr.next
                curr.next=None
                break


            
            curr.next=l[ptr1]
            curr=curr.next
            ptr1+=1
            if ptr2<=ptr1:
                curr.next=l[ptr2]
                curr=curr.next
                curr.next=None
                break
            
            



def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.reorderList(input1)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)



if __name__ == "__main__":
    # case 1 : 1234567->1726354
    a=ListNode(1)
    b=a.next=ListNode(2)
    c=b.next=ListNode(3)
    d=c.next=ListNode(4)
    e=d.next=ListNode(5)
    f=e.next=ListNode(6)
    g=f.next=ListNode(7)

    s = Solution()
    test_driver(s,a,None,'none')
    curr=a
    while curr:
        print(curr.val)
        curr=curr.next
    
    # case 2 : 1->1
    a=ListNode(1)
    
    s = Solution()
    test_driver(s,a,None,'none')
    curr=a
    while curr:
        print(curr.val)
        curr=curr.next

    # case 3 : 12->12
    a=ListNode(1)
    b=a.next=ListNode(2)
    s = Solution()
    test_driver(s,a,None,'none')
    curr=a
    while curr:
        print(curr.val)
        curr=curr.next
    
    # case 4 : 123->132
    a=ListNode(1)
    b=a.next=ListNode(2)
    c=b.next=ListNode(3)
    s = Solution()
    test_driver(s,a,None,'none')
    curr=a
    while curr:
        print(curr.val)
        curr=curr.next
    
