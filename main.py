class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)
        if n==1:return True
        visited=[False]*n
        
        curr=0
        while True:
            visited[curr]=True
            stride=nums[curr]

            low=0 if curr-stride<0 else curr-stride
            high=n-1 if curr+stride>n-1 else curr+stride
            my_reach=range(low,high+1)
            
            index_2_jump=None
            _max_stride=0
            for i in my_reach:
                if _max_stride<=nums[i] and not visited[i]:
                    _max_stride=nums[i]
                    index_2_jump=i
            curr=index_2_jump
            if curr==n-1:return True
            elif nums[curr]==0:return False

        


def test_case(input,expected):
    sol = Solution()
    res=sol.canJump(input)
    expected=True
    print(res," ", expected)

if __name__ == "__main__":
    t=[]
    input=[2,3,1,1,4]
    expected=True
    t.append((input,expected))
    input=[3,2,1,0,4]
    expected=False
    t.append((input,expected))
    input=[2,0,1,1,4,2,1,1,10]
    expected=True
    t.append((input,expected))
    input=[0,2,3]
    expected=False
    t.append((input,expected))
    input=[3,2,1,0,4]
    expected=False
    t.append((input,expected))
    input=[5,9,3,2,1,0,2,3,3,1,0,0]
    expected=True
    t.append((input,expected))
    for test in t:
        test_case(test[0],test[1])
