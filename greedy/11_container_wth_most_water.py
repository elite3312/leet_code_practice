class Solution:
    def maxArea(self, height: list[int]) -> int:
        n=len(height)
        curr_left=0
        curr_right=n-1
        curr_max_vol=0
        #curr_best_left=0
        #curr_best_right=n-1
        while True:
            #check end condition
            if curr_right==curr_left:break

            curr_offset=curr_right-curr_left
            move_left_index=False
            _min_height=None
            if height[curr_left]>=height[curr_right]:
                _min_height=height[curr_right]
                
            else:
                _min_height=height[curr_left]
                move_left_index=True
            _curr_vol=_min_height*curr_offset
            #update curr_max_vol, curr_best_left, curr_best_right
            if curr_max_vol<_curr_vol:
                curr_max_vol=_curr_vol
                #curr_best_left=curr_left
                #curr_best_right=curr_right

            #move curr_left or curr_right
            if move_left_index:
                curr_left+=1
            else:
                curr_right-=1
             
        return curr_max_vol
if __name__ == "__main__":
    s=Solution()
    height = [1,8,6,2,5,4,8,3,7]#49
    print(s.maxArea(height))
    