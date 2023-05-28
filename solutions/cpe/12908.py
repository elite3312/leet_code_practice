'''
On February 18, 2014, Red Matemática proposed the following mathematical challenge on their twitter
account (@redmatematicant): “While Anita read: The book thief by Markus Zusak, She added all the
page numbers starting from 1. When she finished the book, she got a sum equal to 9.000 but she
realized that one page number was forgotten in the process. What is such number? and, how many
pages does the book have?”
Using this interesting puzzle as our starting point, the problem you are asked to solve now is: Given
a positive integer s (1 ≤ s ≤ 108
) representing the result obtained by Anita, find out the number of the
forgotten page and the total number of pages in the book.
Input
The input may contain several test cases. Each test case is presented on a single line, and contains
one positive integer s. The input ends with a test case in which s is zero, and this case must not be
processed.
Output
For each test case, your program must print two positive integers denoting the number of the forgotten
page and the total number pages in the book. Each valid test case must generate just one output line.
'''
class Solution:
    def __init__(self) -> None:
        self.sums=[1]
        for upper in range(2,300):
            sum=int((1+upper)*upper/2)
            self.sums.append(sum)

    def page_number(self , sum):
       

        index=-1
        for i in range(0,299):
            if self.sums[i]>sum:
                index=i
                break
        diff=self.sums[index]-sum
        return (diff,index+1)
    
def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.page_number(input1)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)


if __name__ == "__main__":

    s = Solution()

    test_driver(s,1, None,[2,2])
    test_driver(s,9000, None,[45, 134])
    test_driver(s,499977, None,[523 , 1000])


