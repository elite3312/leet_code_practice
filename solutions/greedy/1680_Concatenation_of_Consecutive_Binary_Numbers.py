

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        curr_binary = '1'
        res = ''
        res += curr_binary
        for i in range(1, n):

            if curr_binary.endswith('1'):
                index = -1
                is_all_one = False
                while (True):
                    if curr_binary[index] == '0':
                        break
                    index -= 1
                    if index == -(len(curr_binary)+1):
                        is_all_one = True
                        break
                if is_all_one:
                    curr_binary = '1'+'0'*len(curr_binary)
                else:
                    curr_binary = curr_binary[:index]+'1'+'0'*(-1-index)
            else:
                curr_binary = curr_binary[:-1]+'1'
            res += curr_binary
        res=int(res,2) % 1000000007
        return res


if __name__ == "__main__":

    s = Solution()
    # n=3
    # n=4
    n =12
    ans = s.concatenatedBinary(n)
    print(ans)
    ans = "1101110010111011110001001101010111100"
    print(ans)
