try:
    from utils.test_driver import test_driver
except:
    pass
import heapq
class Solution:
    def b(self, records) -> int:
        a_max_temp=2e9+87
        b_max_temp=2e9+87
        a_max=2e9+87
        b_max=2e9+87
        
        for r in records:
            if r[-1]==False:
                a_max=r[0]+1
                b_max=r[1]+1
            else:
                a_max_temp=max(min(a_max_temp,r[0]),1)
                b_max_temp=max(min(b_max_temp,r[0]),1)
        
        a=min(a_max)
        b=b_max
        res=[a,b,max(a,b)]
        return res



if __name__ == "__main__":
    s = Solution()

    submit = False
    index = 0

    if submit:
        n = str(input()).strip()
        n = int(n)

        records = []
        for i in range(n):
            cur = str(input()).strip().split(' ')
            if cur[-1] == "True":
                cur[-1] = True
            else:
                cur[-1] = False
            records.append(cur)

        res = s.b()

        print(res)

    else:
        input0=[[1, 2 ,True],
                [2, 1,True],
                [5, 0,False]]
        res0    =[6,1,6]
        tests = [
            [
                input0,
                res0,
            ],
            [
                [[0,1 ,True],
                [1,0,True],],
                [1,1,1]
            ]
        ]

        for input, res in tests[index:]:
            test_driver(s.b, input, expected=res)
