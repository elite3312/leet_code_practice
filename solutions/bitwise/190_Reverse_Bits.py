class Solution:
    def reverseBits(self, n: int) -> int:
        bit_str="{0:b}".format(n)
        if len(bit_str)>32:return -1
        elif len(bit_str)<32:
            bit_str='0'*(32-len(bit_str))+bit_str
        bit_str=bit_str[::-1]#reverse

        return int(bit_str,2)
def test_driver(s: Solution, *inputs, expected: str):
    # change this line
    ans = s.reverseBits(*inputs)

    for i in range(len(inputs)):
        print('input_%d : %s'%(i,str(inputs[i])))
    print("ans: ", ans)
    print('expected:', expected)
if __name__ == "__main__":
    s = Solution()
    test_driver(s, 43261596, expected=964176192)
    '''
    Input: n = 00000010100101000001111010011100
    Output:    964176192 (00111001011110000010100101000000)
    Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
    so return 964176192 which its binary representation is 00111001011110000010100101000000.
    '''
    test_driver(s, 4294967293, expected=3221225471)
    '''
    Input: n = 11111111111111111111111111111101
    Output:   3221225471 (10111111111111111111111111111111)
    Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, 
    so return 3221225471 which its binary representation is 10111111111111111111111111111111.
    '''