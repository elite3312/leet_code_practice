from utils.test_driver import test_driver


class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        def is_strictly_increasing(test_list):
            res = all(i < j for i, j in zip(test_list, test_list[1:]))
            return res
        res=1
        n=len(nums)
        for sub_arr_len in range(1,n):
            sub_arr_len_indices=[(i,i+sub_arr_len) for i in range(n-sub_arr_len+1)]
            for sub_arr_len_indice in sub_arr_len_indices:
                new_l=nums[:sub_arr_len_indice[0]]+nums[sub_arr_len_indice[1]:]
                if is_strictly_increasing(new_l):res+=1
        return res

if __name__ == "__main__":
    s = Solution()

    tests = [
            [[1,2,3,4],10],
            [[6,5,7,8],7],
            [[8,7,6,6],3],
        ]
    for input, res in tests:
        test_driver(s.incremovableSubarrayCount, input, expected=res)
