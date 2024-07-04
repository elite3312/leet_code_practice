class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(l:ListNode):
    res=[]
    while l!=None:
        res.append(str(l.val))
        l=l.next
    res=" ".join(res)
    print(res)
    return  res