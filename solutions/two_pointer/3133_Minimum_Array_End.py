from utils.test_driver import test_driver


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bin_x=list(bin(x)[2:])
        bin_len=len(bin_x)
        # 1xxx1xxx1xx, given that the '1's must stay the same, find the nth biggest value
        
        dont_care_cnt=0
        for _ in bin_x:
            if _ =='0':dont_care_cnt+=1

        bin_n=list(bin(n-1)[2:])# we minus one from n since x itself contributes to the first bin
        bin_n_len=len(bin_n)

        res=bin_x.copy()
        if len(bin_n)>dont_care_cnt:
            i=bin_len-1
            j=bin_n_len-1
            while i>-1:
                if bin_x[i]=='0':
                    res[i]=bin_n[j]
                    i-=1
                    j-=1
                else:
                    i-=1
            res=bin_n[:j+1]+res
        else:
            i=bin_len-1
            j=bin_n_len-1
            while j>-1:
                if bin_x[i]=='0':
                    res[i]=bin_n[j]
                    i-=1
                    j-=1
                else:
                    i-=1
        res=''.join(res)
        return int(res,2)



        



        

if __name__ == "__main__":

    s = Solution()
    index=1
    n = 3
    x = 4
    res=6
    tests = [
        [
            # inputs
            [
              n,x
            ],
            # res
            res
            
        ],
       
        [
            # inputs
            [
              2,7
            ],
            # res
            15
            
        ],
        [
            # inputs
            [
              1,3
            ],
            # res
            3
            
        ],
        [
            # inputs
            [
              3,1
            ],
            # res
            5
            
        ],
        [
            # inputs
            [
              3,2
            ],
            # res
            6
            
        ],
        [
            # inputs
            [
              4,1
            ],
            # res
            7
            
        ],
    ]
    for input, res in tests[index:]:
        test_driver(s.minEnd, input[0],input[1],   expected=res)
