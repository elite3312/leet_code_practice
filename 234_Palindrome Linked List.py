# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head:ListNode ) -> bool:
        stack=[]
        while True:
            stack.append(head.val)
            if head.next is not None:
                head=head.next
            else:break
        if(len(stack)==1):return True
        if(len(stack)%2==1):
            for i in range((len(stack)-1)//2):
                if(stack[i]!=stack[-(i+1)]):return False
        elif(len(stack)%2==0):
            for i in range(len(stack)//2):
                if(stack[i]!=stack[-(i+1)]):return False
        return True