try:
    from utils.test_driver import test_driver
except:
    pass
'''
individuals will experience stomach ache if and only if at least one of the following conditions occurs:
    ate at least a shrimp
    ate at least b oysters
    ate at least c shrimps and oysters in total
'''


class Solution:
    def b(self, records) -> int:
        a_min,a_max=1,2e9+87
        b_min,b_max=1,2e9+87
        c_min,c_max=1,2e9+87
        c_max_changed=False
        # set lower bounds
        for r in records:
            if r[-1]==False:
                a_min=max(a_min,r[0]+1)
                b_min=max(b_min,r[1]+1)
                c_min=max(c_min,r[0]+r[1]+1)
        # set upper bounds
        for r in records:
            if r[-1]==True:
                if r[0]>=a_min:a_max=min(a_max,r[0])
                if r[1]>=b_min:b_max=min(b_max,r[1])
                if (r[0]+r[1])>=c_min:
                    c_max_changed=True
                    c_max=min(c_max,r[0]+r[1])

        a,b,c=None,None,None
        if a_max==a_min:
            a=a_max
            b=b_min
            c=c_min
        elif b_max==b_min:
            b=b_max
            a=a_min
            c=c_min
        elif c_max==c_min:
            c=c_max
            a=a_min
            b=b_min
        if a==None and b==None and c==None:
            if c_max_changed:
                a=a_min
                b=b_min
                c=c_max
            else:
                return [-1]
        return [a,b,c]


if __name__ == "__main__":
    s = Solution()

    submit = False
    index = 0

    if not submit:
        tests = [
            [
                [[1, 2, True],
                 [2, 1, True],
                 [5, 0, False]],
                [6, 1, 6],
            ],
            [
                [[1, 0 ,True],
                 [0, 1 ,True]],
                [1,1,1],
            ],
            [
                [[1000000000, 1000000000 ,True],
                 [0, 0 ,True]],
                [-1],
            ],
            [
                [[8, 0, True],
                 [7, 0, False],
                 [3, 5, False],
                 [6, 8, True]],
                [8, 8, 14],
            ],
            [
                [
                 [100, 0, False],
                 [60, 60, True],
                 [0, 100, False]],
                [-1],
            ],
        ]
        for input, res in tests[index:]:
            test_driver(s.b, input, expected=res)

    else:
        n = str(input()).strip()
        n = int(n)

        records = []
        for i in range(n):
            cur = str(input()).strip().split(' ')
            if cur[-1] == "True":
                cur[-1] = True
            else:
                cur[-1] = False
            cur[0]=int(cur[0])
            cur[1]=int(cur[1])
            records.append(cur)

        res = s.b(records)
        for _ in range(len(res)):res[_]=str(res[_])
        res=" ".join(res)
        print(res)
