from utils.test_driver import test_driver

from collections import Counter
class Solution:
    def minimumArrayLength(self, nums: list[int]) -> int:
        c=Counter()
        for n in nums:
            c[n]+=1
        sorted_keys=sorted(list(c.keys()))
        
        l=[]
        for k in sorted_keys:
            l.append((k,c[k]))
        while 1:
            if len(l)>2:
                _,top_count=l[-1]
                _,sec_top_count=l[-2]
                remain_index=-1
                new_count=abs(top_count-sec_top_count)
                if top_count>sec_top_count:
                    remain_index=-2
                _=l[remain_index]
                l=l[:len(l)-2]
                l.append(_)



            else:
                if l[0][1]==l[1][1]:return 1
                else:
                    if abs(l[0][1]-l[1][1])==1:return 1
                    elif abs(l[0][1]-l[1][1])%2==1:return 2
                    else :return 1




        

        
if __name__ == "__main__":
    s = Solution()

    tests = [
            [  # case 1
                # inputs
                [
                   [1,4,3,1]
                ],
                # res
                1

            ],
            [  # case 2
                # inputs
                [
                   [5,5,5,10,5]
                ],
                # res
                2

            ],
            [  # case 3
                # inputs
                [
                   [2,3,4]
                ],
                # res
                1

            ],
       

    ]
    for input, res in tests:
        test_driver(s.minimumArrayLength, input[0], expected=res)
