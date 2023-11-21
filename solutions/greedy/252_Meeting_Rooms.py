class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key= lambda x:x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:return False
        return True

                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()

    inp= [[7,10],[2,4]]
    out=True
    test_driver(s.canAttendMeetings,inp,expected=out)
    inp=[[0,30],[5,10],[15,20]]
    out=False
    test_driver(s.canAttendMeetings,inp,expected=out)
