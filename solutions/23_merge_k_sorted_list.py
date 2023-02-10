import heapq
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: list[ListNode]) ->ListNode:
        if len(lists)==0:return
        curr=ListNode(val=10001)
        head=curr
        _my_heap=[]
        # prepare a time stamp for items going into heap
        _time_stamp:int=0

        # add all list heads into heapq
        for l in lists:
            if l!=None:
                heapq.heappush(_my_heap,(l.val,_time_stamp,l))# make sure instances of ListNodes don't get compared!!! Otherwise this will crash.
                _time_stamp+=1
        while True:
            #if heap is empty, break
            if len(_my_heap)==0:
                break
            #find smallest elem in heap, add it into res, and point that elem to its next
            _smallest_tuple:tuple=heapq.heappop(_my_heap)
            curr.next=_smallest_tuple[2]
            curr=curr.next
            
            _next_node=_smallest_tuple[2].next
            if _next_node!=None:
                heapq.heappush(_my_heap,(_next_node.val,_time_stamp,_next_node))
                _time_stamp+=1
        return head.next


if __name__ == "__main__":
    sol=Solution()
    lists=[[1,4,5],[1,3,4],[2,6]] 


    print(sol.mergeKLists(lists))
    