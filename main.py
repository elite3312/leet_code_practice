#wrongs
class MyCalendarThree:

    def __init__(self):

        self.books = []
    def check_intersect_for_2_points(self,p1:tuple,p2:tuple):
        if p1[0]<=p2[1]<=p1[1] or p1[0]<=p2[0]<=p1[1]:return True
        return False

    def book(self, start: int, end: int) -> int:
        self.books.append((start, end-1))
        #self.books.sort()
        res = -1

        for i in range(len(self.books)):
            anchor=self.books[i]
            points_that_intersect_with_anchor=[]
            for j in range(len(self.books)):
                candidate=self.books[j]
                if i == j:
                    continue
                if self.check_intersect_for_2_points(anchor,candidate):
                    failed_check=False
                    for p in points_that_intersect_with_anchor:
                        if not self.check_intersect_for_2_points(candidate,p):
                            failed_check=True
                            break
                    if not failed_check:
                        points_that_intersect_with_anchor.append(candidate)
            res=max(res,len(points_that_intersect_with_anchor)+1)

        return res


def case1():
    '''Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]'''
    s = MyCalendarThree()

    ans = s.book(10, 20)
    print(ans)
    ans = s.book(50, 60)
    print(ans)
    ans = s.book(10, 40)
    print(ans)
    ans = s.book(5,15)
    print(ans)
    ans = s.book(5, 10)
    print(ans)
    ans = s.book(25, 55)
    print(ans)

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
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