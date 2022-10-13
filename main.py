
class Node:
    def __init__(self, l, r, count):
        self.l = l
        # the point that partition the interval, initial there is no partition
        self.mid_point = None
        self.r = r
        self.count = count  # number of events that fall in this interval
        self.left = None
        self.right = None


class MyCalendarThree:
    def __init__(self):
        self.root = Node(0, 10**9, 0)
        self.max = 0

    def book(self, start, end):
        self.add_event( start, end,self.root)
        return self.max

    def add_event(self,  start,end,root):
        if root.mid_point != None:
            # this interval is already partitioned, update left, right, or both subtree
            if end <= root.mid_point: self.add_event(start,end,root.left)
            elif start >= root.mid_point: self.add_event(start,end,root.right)
            else:
                self.add_event( start, root.mid_point,root.left)
                self.add_event(root.mid_point, end ,root.right)
            return
        else:  # this interval is not yet partitioned, add some nodes
            if root.l == start and root.r == end:
                root.count += 1
                self.max=max(self.max,root.count)
            elif root.l == start and root.r != end:
                root.mid_point=end
                root.left = Node( start,root.mid_point, root.count+1)
                root.right = Node(root.mid_point, root.r, root.count)
                self.max=max(self.max,root.count+1)
            elif root.l != start and root.r == end:
                root.mid_point=start
                root.left = Node( root.l,root.mid_point, root.count)
                root.right = Node(root.mid_point, root.r, root.count+1)
                self.max=max(self.max,root.count+1)
            elif root.l != start and root.r != end:
                root.mid_point = start
                root.left = Node(root.l, root.mid_point , root.count)
                root.right = Node(root.mid_point, root.r, root.count)
                self.add_event(start, end, root.right)
            


if __name__ == "__main__":
    s = MyCalendarThree()
    ans = s.book(5, 12)
    print(ans)
    ans = s.book(42, 50)
    print(ans)
    ans = s.book(4, 9)
    print(ans)
    ans = s.book(33, 41)
    print(ans)
    ans = s.book(2, 7)
    print(ans)
    ans = s.book(16, 25)
    print(ans)
    ans = s.book(7, 16)
    print(ans)
    ans = s.book(6, 11)
    print(ans)
    ans = s.book(13, 18)
    print(ans)

    ans = s.book(38, 43)
    print(ans)
    ans = s.book(49, 50)
    print(ans)
    ans = s.book(6, 15)
    print(ans)
    ans = s.book(5, 13)
    print(ans)  # 6
