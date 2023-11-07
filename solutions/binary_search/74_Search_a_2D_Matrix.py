'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        new_list=[]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                new_list.append(matrix[r][c])
        return binary_search(new_list,0,len(new_list)-1,target)
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return True
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return False    
    

       
def test_driver(s: Solution, *inputs, expected: str):
    # change this line
    ans = s.searchMatrix(*inputs)

    for i in range(len(inputs)):
        print('input_%d : %s'%(i,str(inputs[i])))
    print("ans: ", ans)
    print('expected:', expected)
if __name__ == "__main__":
    s = Solution()
    matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    test_driver(s, matrix,target, expected=True)

    matrix=[[1, 3,  5, 7],
            [10,11,16,20],
            [23,30,34,60]]
    target = 4
    test_driver(s, matrix,target, expected=False)

# idea : use auxillary array to store matrix, then binary search the array