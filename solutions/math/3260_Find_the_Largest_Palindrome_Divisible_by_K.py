from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
#from itertools import combinations
# from collections import Counter
# from collections import deque
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
    
        if n == 1:
            for i in range(9, 0, -1):
                if i % k == 0:
                    return str(i)
            return -1
        if k in [1,3,9]:
            return '9'*n
        elif k ==2 :
            if n <= 2:
                return '8' * n
            else:
                return '8' + '9' * (n - 2) + '8'
        elif k == 4:
            if n <= 4:
                return '8' * n
            else:
                return '88' + '9' * (n - 4) + '88'
        elif k==5:
            if n <= 2:
                return '5' * n
            else:
                return '5' + '9' * (n - 2) + '5'
        elif k == 6:
            if n <= 2:
                return '6' * n
            elif n % 2 == 1:
                l = n // 2 - 1
                return '8' + '9' * l + '8' + '9' * l + '8'
            else:
                l = n // 2 - 2
                return '8' + '9' * l + '77' + '9' * l + '8'
        elif k == 8:
            if n <= 6:
                return '8' * n
            else:
                return '888' + '9' * (n - 6) + '888'
        elif k==7:
            dic = {0: '', 1: '7', 2: '77', 3: '959', 4: '9779', 5: '99799', 6: '999999', 7: '9994999',
                       8: '99944999', 9: '999969999', 10: '9999449999', 11: '99999499999'}
            l, r = divmod(n, 12)
            return '999999' * l + dic[r] + '999999' * l
            
    def largestPalindrome_1(self, n: int, k: int) -> str:
    
        if n == 1:
            for i in range(9, 0, -1):
                if i % k == 0:
                    return str(i)
            return -1
        def construct_palindrome(half, odd):
            if odd:
                return int(half + half[-2::-1])#aaabb
            else:
                return int(half + half[::-1])#aabb
        
        
        half_length = (n + 1) // 2
        largest_half = '9' * half_length
        largest_palindrome = construct_palindrome(largest_half, n % 2)
        
        while largest_palindrome % k != 0:
            largest_half = str(int(largest_half) - 1)
            largest_palindrome = construct_palindrome(largest_half, n % 2)
        
        return str(largest_palindrome)
    
    def largestPalindrome_0(self, n: int, k: int) -> str:
        def is_palindrome(x):
            return str(x) == str(x)[::-1]
        
        # Start from the largest n-digit number
        largest_n_digit = 10**n - 1
        
        for num in range(largest_n_digit, 10**(n-1) - 1, -1):
            if is_palindrome(num) and num % k == 0:
                return num
    
        return -1
if __name__ == "__main__":
    
    #1 <= n <= 105
    #1 <= k <= 9
    
    sol = Solution()

    index = 0

    tests = [
        [[4,2],'8888'],
        [
          [3,5]  ,'595'
        ],
        [
          [3,3]  ,'999'
        ],
    ]

    test_driver_main(sol.largestPalindrome, tests, index)
