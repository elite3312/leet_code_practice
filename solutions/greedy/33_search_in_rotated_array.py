class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        upper = len(nums) - 1
        n=len(nums) - 1
        while low <= upper:

            if low==upper and nums[low]!=target:
                return -1

            mid = (low + upper) // 2
            if nums[mid] == target:
                return mid
            
            #find left subset boundaries
            left_low=low
            left_upper=mid-1
            if left_upper<left_low:
                left_upper=left_low

            #find right subset boundaries
            right_low=mid+1
            right_upper=upper

            if right_low>right_upper:
                right_low=right_upper

            # if the left subset is not strictly increasing, then the right subset must contain the cut point
            if nums[left_low]<=nums[left_upper]:
                # check if target is in the left subset
                if nums[left_low]<=target<= nums[left_upper]:
                    upper=left_upper
                else:# target is in the right subset 
                    low=right_low
            else: #the right subset is strictly increasing, thus the left subset must contain the cut point
                # check if target is in the right subset
                if nums[right_low]<=target<= nums[right_upper]:
                    low=right_low
                else:# target is in the left subset 
                    upper=left_upper
        return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(sol.search(nums, 0),4)

    nums = [3, 1]
    print(sol.search(nums, 2),-1)

    nums = [ 1,3]
    print(sol.search(nums, 0),-1)

    nums = [ 1]
    print(sol.search(nums, 0),-1)

    nums = [ 4,5,6,7,8,1,2,3]
    print(sol.search(nums, 8),4)

    nums=[6,7,1,2,3,4,5]
    print(sol.search(nums, 6),0)

    nums=[2,3,4,5,6,7,8,9,1]
    print(sol.search(nums, 9),7)

    nums=[3,4,5,6,7,8,1,2]
    print(sol.search(nums, 2),7)