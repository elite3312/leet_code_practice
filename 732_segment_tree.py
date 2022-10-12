"""
Author: Huahua
Runtime: 436 ms (<88.88%)
"""
class Node:
    def __init__(self, l, r, count):
        self.l = l
        self.m = -1#mid point
        self.r = r            
        self.count = count#number of intersections
        self.left = None
        self.right = None
            
class MyCalendarThree:        
    def __init__(self):
        self.root = Node(0, 10**9, 0)
        self.max = 0
 
    def book(self, start, end):
        self.add(start, end, self.root)
        return self.max
    
    def add(self, start, end, root):
        if root.m != -1:
            if end <= root.m: self.add(start, end, root.left)
            elif start >= root.m: self.add(start, end, root.right)
            else:
                self.add(start, root.m, root.left)
                self.add(root.m, end, root.right)
            return
        
        if start == root.l and end == root.r:
            root.count += 1
            self.max = max(self.max, root.count)
        elif start == root.l:
            root.m = end
            root.left = Node(start, root.m, root.count + 1)
            root.right = Node(root.m, root.r, root.count)
            self.max = max(self.max, root.count + 1)
        elif end == root.r:
            root.m = start
            root.left = Node(root.l, root.m, root.count)
            root.right = Node(root.m, root.r, root.count + 1)
            self.max = max(self.max, root.count + 1)
        else:
            root.m = start
            root.left = Node(root.l, root.m, root.count)
            root.right = Node(root.m, root.r, root.count)
            self.add(start, end, root.right)
            
if __name__=="__main__":
    '''["MyCalendarThree","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"]
    [[],[5,12],[42,50],[4,9],[33,41],[2,7],[16,25],[7,16],[6,11],[13,18],[38,43],[49,50],[6,15],[5,13],[35,42],[19,24],[46,50],[39,44],[28,36],[28,37],[20,29],[41,49],[11,19],[41,46],[28,37],[17,23],[22,31],[4,10],[31,40],[4,12],[19,26]]'''
    
    '''expected
    [null,1,1,2,2,3,3,3,4,4,4,4,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,8,8]'''
    '''output
    [null,1,1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,7,7]'''
    s = MyCalendarThree()
    ans = s.book(5,12)
    print(ans)
    ans = s.book(42,50)
    print(ans)
    ans = s.book(4, 9)
    print(ans)
    ans = s.book(33,41)
    print(ans)
    ans = s.book(2, 7)
    print(ans)
    ans = s.book(16 ,25)
    print(ans)
    ans = s.book(7 ,16)
    print(ans)
    ans = s.book(6 ,11)
    print(ans)
    ans = s.book(13 ,18)
    print(ans)
    
    ans = s.book(38 ,43)
    print(ans)
    ans = s.book(49,50)
    print(ans)
    ans = s.book(6,15)
    print(ans)
    ans = s.book(5 ,13)
    print(ans)#6