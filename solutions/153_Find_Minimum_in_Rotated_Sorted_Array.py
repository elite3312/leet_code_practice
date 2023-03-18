class Solution:
    def findMin(self, nums: list[int]) -> int:
        cut_point = self.find_cut_point(nums)
        if cut_point == -1:
            return nums[0]
        return nums[cut_point+1]

    def find_cut_point(self, nums: list[int]):
        '''
        we define the cutpoint as follows: 
            If the array was rotated [1,n-1] times,
            then the cutpoint = x if and only if nums[x]>nums[x+1] for x in[0,n-1]
            Note that nums[x] is the maximum of nums.
        '''
        n = len(nums)
        # edge case: rotated n times or n==1, cutpoint is non existent
        if n == 1:
            return -1
        if nums[0] < nums[n-1]:
            return -1

        # cut point exists
        low = 0
        upper = len(nums) - 1

        while 1:
            mid = (low + upper) // 2
            # low should never be equal to upper, at most low==upper-1
            if nums[mid] > nums[mid+1]:
                return mid
            # left subset= nums[low:mid]
            # find left subset boundaries
            left_low = low
            left_upper = mid-1
            if left_upper < left_low:
                left_upper = left_low

            # right subset= nums[mid:]
            # find right subset boundaries
            right_low = mid
            right_upper = upper
            if right_low > right_upper:
                right_low = right_upper

            # ----------do checks------------#

            # if left_low==left_upper
            if left_low == left_upper:
                if nums[left_upper] > nums[mid]:
                    return left_low  # found cut_point
                else:
                    low = right_low  # cut_point is in right subset

            # if right_low==right_upper
            elif right_low == right_upper:
                if nums[mid] > nums[right_low]:
                    return mid  # found cut_point
                else:
                    upper = left_upper  # cut_point is in left subset

            # if the left subset is strictly increasing
            elif nums[left_low] < nums[left_upper]:
                if nums[left_upper] > nums[mid]:
                    return left_upper  # found cut_point
                else:
                    low = right_low  # cut_point is in right subset

            # the right subset is strictly increasing
            else:
                if nums[mid] > nums[right_low]:
                    return mid
                else:
                    upper = left_upper  # cut_point is in left subset


if __name__ == "__main__":
    s = Solution()

    input1 = [4, 5, 1, 2, 3]
    expected_cutpoint = 1
    expected_min = 1
    print("cut point index: %d" % s.find_cut_point(input1),
          "expected_cutpoint:%d" % expected_cutpoint)
    print('min=%d' % s.findMin(input1), 'expected_min:%d' % expected_min)

    input1 = [3, 1, 2]
    expected_cutpoint = 0
    expected_min = 1
    print("cut point index: %d" % s.find_cut_point(input1),
          "expected_cutpoint:%d" % expected_cutpoint)
    print('min=%d' % s.findMin(input1), 'expected_min:%d' % expected_min)

    input1 = [3, 4, 5, 1, 2]
    expected_cutpoint = 2
    expected_min = 1
    print("cut point index: %d" % s.find_cut_point(input1),
          "expected_cutpoint:%d" % expected_cutpoint)
    print('min=%d' % s.findMin(input1), 'expected_min:%d' % expected_min)

    input1 = [1, 0]
    expected_cutpoint = 0
    expected_min = 0
    print("cut point index: %d" % s.find_cut_point(input1),
          "expected_cutpoint:%d" % expected_cutpoint)
    print('min=%d' % s.findMin(input1), 'expected_min:%d' % expected_min)
