
class Solution:
    def continued_fraction(self , numerator,denominator):
        res=[]
        
        right_part=1
        while 1:
            left_part=numerator//denominator # 2
            right_part=numerator%denominator # 5
            res.append(left_part)
            if right_part==0:break
            numerator=denominator
            denominator=right_part
        return res



 
    

def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.continued_fraction(input1,input2)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)


if __name__ == "__main__":

    s = Solution()

    test_driver(s,43, 19,[2,3,1,4])

