# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        curr=head
        if curr==None:return False
        if head.next:
            curr_faster=head.next.next
        else:return False

        while 1:
            if curr==None:return False
            if curr_faster==None:return False

            if curr==curr_faster:return True

            curr=curr.next
            if curr_faster.next:
                curr_faster=curr_faster.next.next
            else:
                return False
    def hasCycle_space_n(self, head: ListNode) -> bool:
        #The number of the nodes in the list is in the range [0, 1e4].
        id_dict={}
        while 1:
            if head ==None:
                return False
            if id_dict.get(id(head)):
                return True
            id_dict[id(head)]=True                
            head=head.next
def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.hasCycle(input1)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)



if __name__ == "__main__":

    s = Solution()
    
    
