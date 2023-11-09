class Solution:
    #  1_3
    #   2_4
    #   2__5
    #    3__6
    #->1____6

    # 1__4
    #  23
    #->1__4

    # o(n)
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
    
    input=[[1,3],[2,6],[8,10],[15,18]]
    expected=[[1,6],[8,10],[15,18]]
    print(s.merge(input),' ans=',expected) 

    input=[[1,4],[4,5]]
    expected=[[1,5]]
    print(s.merge(input),' ans=',expected)   
    
    input=[[1,3],[2,4],[2,5],[3,6]]
    expected=[[1,6]]
    print(s.merge(input),' ans=',expected)   

    input=[[1,3],[2,4],[2,5],[3,6],[19,20]]
    expected=[[1,6],[19,20]]
    print(s.merge(input),' ans=',expected)   

    input=[[1,5]]
    expected=[[1,5]]
    print(s.merge(input),' ans=',expected)   

    input=[[1,1],[1,2],[1,3],[1,4],[5,5]]
    expected=[[1,5]]
    print(s.merge(input),' ans=',expected)   

    input=[[1,2],[2,2],[3,3],[4,4],[5,5]]
    expected=[[1,5]]
    print(s.merge(input),' ans=',expected)   
    
    input=[[1,4],[2,3]]
    expected=[[1,4]]
    print(s.merge(input),' ans=',expected)  