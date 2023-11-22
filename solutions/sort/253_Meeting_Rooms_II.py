class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
       # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0
        num_rooms = 0
        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted(i[0] for i in intervals)
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)
        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0
        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            #print(start_timings[start_pointer],end_timings[end_pointer])
            if start_timings[start_pointer] < end_timings[end_pointer]:
            # Free up a room and increment the end_pointer.
                num_rooms += 1
            else:
                end_pointer += 1
            start_pointer += 1
        return num_rooms
                                        
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()

    inp=[[0, 30],[5, 10],[15, 20]]
    out=2
    test_driver(s.minMeetingRooms,inp,expected=out)
    