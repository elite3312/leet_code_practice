class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)
        if n==1:return True
        goal_lists=dict()#goal_lists[i] : a list containing possible starting jump points that go to land at i
        for i in range(n):
            goal_lists[i]=[]
        goal_lists[0].append(0)

        for index,elem in enumerate(nums[:n-1]):
            can_reach_farthest=index+elem
            if can_reach_farthest>=n-1:
                can_reach_farthest=n-1
            goal_lists[can_reach_farthest].append(index)

        #for _list in goal_lists:
            #_list.sort()
        

        curr_goal=n-1
        prev_curr_goal=n
        while True:
            while True:
                curr_max_reach=nums[curr_goal]
                if len(goal_lists[curr_goal])!=0:
                    break
                else: curr_goal+=1
                if curr_goal>curr_goal+curr_max_reach:
                    return False
                if curr_goal==prev_curr_goal:
                    return False
            prev_curr_goal=curr_goal
            curr_goal=goal_lists[curr_goal][0]
            if curr_goal==0:
                return True
            else:
                if prev_curr_goal==curr_goal:
                    return False

def case_1():
    sol = Solution()
    n=[2,3,1,1,4]
    res=sol.canJump(n)
    expected=True
    print(res," ", expected)
def case_2():
    sol = Solution()
    n=[3,2,1,0,4]

    res=sol.canJump(n)
    expected=False
    print(res," ", expected)
def case_3():
    sol = Solution()
    n=[2,0,1,1,4,2,1,1,10]

    res=sol.canJump(n)
    expected=True
    print(res," ", expected)
def case_4():
    sol = Solution()
    n=[0,2,3]

    res=sol.canJump(n)
    expected=False
    print(res," ", expected)
def case_5():
    sol = Solution()
    n=[3,2,1,0,4]

    res=sol.canJump(n)
    expected=False
    print(res," ", expected)
#[5,9,3,2,1,0,2,3,3,1,0,0]
def case_6():
    sol = Solution()
    n=[5,9,3,2,1,0,2,3,3,1,0,0]

    res=sol.canJump(n)
    expected=True
    print(res," ", expected)
if __name__ == "__main__":
    #case_1()
    #case_2()
    #case_3()
    #case_4()
    #case_5()
    case_6()
