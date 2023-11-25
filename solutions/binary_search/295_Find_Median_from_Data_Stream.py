from utils.test_driver import test_driver
from collections import deque

class MedianFinder:

    def __init__(self):
        self.list=deque()

    def addNum(self, num: int) -> None:
        l=self.list
        n=len(self.list)
        if n==0:
            l.append(num)
  
        else:
            if l[0]>=num:l.insert(0,num)
            elif num>=l[-1]:l.append(num)
            else:
                # binary search the appropriate index
                left=0
                right=n-1
                while right>=left:
                    mid=(left+right)//2
                    if l[mid]<=num and num<=l[mid+1]:
                        l.insert(mid+1,num)
                        break
                    elif num <= l[mid]:
                        right=mid-1
                    else:
                        left=mid+1




    def findMedian(self) -> float:
        mid=len(self.list)//2
        if len(self.list)%2==1:
            return self.list[mid]
        else:
            return (self.list[mid]+ self.list[mid-1])/2
class MedianFinder_tle:

    def __init__(self):
        self.list=deque()

    def addNum(self, num: int) -> None:
        l=self.list
        n=len(self.list)
        if n==0:
            l.append(num)
        elif n==1:
            if num>l[0]:l.append(num)
            else:
                l.insert(0,num)
        else:
            if num<=l[0]:l.insert(0,num)
            elif num>=l[-1]:l.append(num)
            else:
                for i in range(n-1):
                    if l[i]<=num and num<=l[i+1]:
                        l.insert(i+1,num)
                        break



    def findMedian(self) -> float:
        mid=len(self.list)//2
        if len(self.list)%2==1:
            return self.list[mid]
        else:
            return (self.list[mid]+ self.list[mid-1])/2
if __name__=='__main__':
    m=MedianFinder()
    m.addNum(6)
    m.addNum(10)
    m.addNum(2)
    m.addNum(6)
    test_driver(m.findMedian,expected=6)
    m=MedianFinder()
    m.addNum(-1)
    m.addNum(-2)
    m.addNum(-3)
    m.addNum(-4)
    m.addNum(-5)
    test_driver(m.findMedian,expected=-3)

    m=MedianFinder()
    m.addNum(1)
    m.addNum(2)
    m.addNum(3)
    test_driver(m.findMedian,expected=2)
# idea: 1. use a deque() to store nums so far.
# 2. use binary search to look for appropriate index to insert, thereby keeping the numbers sorted.
# 3. median can be found directly from sorted list