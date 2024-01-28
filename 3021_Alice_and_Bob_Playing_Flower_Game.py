
from utils.test_driver import test_driver




class Solution_tle:
    def count_even_numbers(self,n):
        if n < 2:
            return 0  # There are no even numbers if n is less than 2
        
        # If n is odd, subtract 1 to make it even
        if n % 2 != 0:
            n -= 1
        
        # Calculate the number of even numbers by dividing n by 2
        count = n // 2
        return count
    def count_odd_numbers(self,n):
        if n < 1:
            return 0  # There are no odd numbers if n is less than 1
        
        # If n is even, subtract 1 to make it odd
        if n % 2 == 0:
            n -= 1
        
        # Calculate the number of odd numbers by dividing n by 2 and adding 1
        count = (n // 2) + 1
        return count
    def flowerGame(self, n: int, m: int) -> int:
        res=0

        n,m=min(n,m),max(n,m)
        
        for i in range (1,n+1):
            if i%2==1:
                res+=self.count_even_numbers(i)*2
            else:
                res+=self.count_odd_numbers(i)*2
        if n==m:return res
        for y in range(n+1,m+1):
            for x in range (1,n+1):
                if (x+y)%2==1:res+=1
       


        return res

class Solution:
    
    def flowerGame(self, n: int, m: int) -> int:
        res=0

        n,m=min(n,m),max(n,m)
        
        if n %2==1:
            n_odd=(n+1)//2
            n_even=(n-1)//2
        else:
            n_odd=n//2
            n_even=n//2
        if m %2==1:
            m_odd=(m+1)//2
            m_even=(m-1)//2
        else:
            m_odd=m//2
            m_even=m//2
        
       


        return n_odd*m_even+n_even*m_odd       
if __name__ == "__main__":
    s = Solution()

    tests = [
         [
            # inputs
            [
                4,4
            ],
            # res
            8

            # 12 32 21
        ],
        [
            # inputs
            [
                4,3
            ],
            # res
            6

            # 12 32 21
        ],
       
        [
            # inputs
            [
                2,4
            ],
            # res
            4

       
        ],
        [
            # inputs
            [
                3,2
            ],
            # res
            3

            # 12 32 21
        ],
       [
            # inputs
            [
                1,1
            ],
            # res
            0

          
        ],
       




    ]
    for input, res in tests:
        test_driver(s.flowerGame, input[0],input[1] , expected=res)
'''
o(1)
1 alice will win if the (x+y) mod 2 ==1
2 inorder for x+y to be odd, either (x is odd and y is even) or (x is even and y is odd) 
3 use o(1) to find the number of even or odd number less than or eual to x and do the same for y.
4. res= n_odd*m_even+n_even*m_odd 
'''