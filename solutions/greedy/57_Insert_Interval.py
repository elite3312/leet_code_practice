class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        n=len(intervals)
        intervals.append(newInterval)
        
        return self.merge(intervals)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n=len(intervals)
        if n==1:
            return intervals
        intervals.sort()
        res=[]
        
        anchor_left=intervals[0]
        i=1
        while 1:
            
            anchor_right=intervals[i]

            if anchor_left[1]>=anchor_right[0]:
                if anchor_left[1]>=anchor_right[1]:
                    pass
                else:
                    anchor_left[1]=anchor_right[1]
                
            else:
                res.append(anchor_left)
                anchor_left=anchor_right
            i+=1
            if i==n:
                res.append(anchor_left)
                break

        return res
if __name__ == "__main__":
    s=Solution()
    
    input1=[[1,3],[6,9]]
    input2=[2,5]
    expected=[[1,5],[6,9]]
    print(s.insert(input1,input2),' ans=',expected) 

    input1=[[1,2],[3,5],[6,7],[8,10],[12,16]]
    input2=[4,8]
    expected=[[1,2],[3,10],[12,16]]
    print(s.insert(input1,input2),' ans=',expected) 
