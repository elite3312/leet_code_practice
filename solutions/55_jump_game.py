class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)

        # edge cases
        if n==1:return True
        if nums[0]==0:return False
        
        # reaches record the possible jump area of each point
        reaches=[]
        for i in range(n-1):
            stride=nums[i]
            if stride==0 :continue
            low=0 if i-stride<0 else i- stride
            high=n-1 if i+stride>n-1 else i+stride
            reaches.append((i,low,high))#(index, left reach,right reach)
        
        curr_farthest=0#farthest right
        for i in range(len(reaches)):
            #last reach
            if i==len(reaches)-1:
                if reaches[i][2]>=n-1:
                    return True
                else:
                    return False
            # not last reach
            curr_farthest= max(reaches[i][2],curr_farthest)
            if curr_farthest>=n-1:return True
            if curr_farthest<reaches[i+1][0] :return False
            elif curr_farthest==reaches[i+1][0] and nums[ curr_farthest]==0 : return False
        

if __name__ == "__main__":
    s=Solution()
    
    input=[3,1,0,4,3]
    expected=True
    print(s.canJump(input),' ans=',expected) 
    
    input=[5,9,3,2,1,0,2,3,3,1,0,0]
    expected=True
    print(s.canJump(input),' ans=',expected)

    input=[2,0,1,1,4,2,1,1,10]
    expected=True
    print(s.canJump(input),' ans=',expected)

    input=[1,0,2,2,0]
    expected=False
    print(s.canJump(input),' ans=',expected)
    


    input=[1,0,1,0]
    expected=False
    print(s.canJump(input),' ans=',expected)

    input=[2,0,0]
    expected=True
    print(s.canJump(input),' ans=',expected)

    input=[0,1]
    expected=False
    print(s.canJump(input),' ans=',expected)

    input=[2,3,1,1,4]
    expected=True
    print(s.canJump(input),' ans=',expected)

    input=[3,2,1,0,4]
    expected=False
    print(s.canJump(input),' ans=',expected)



    input=[0,2,3]
    expected=False
    print(s.canJump(input),' ans=',expected)

    input=[3,2,1,0,4]
    expected=False
    print(s.canJump(input),' ans=',expected)



