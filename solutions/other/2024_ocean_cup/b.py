try:
    from utils.test_driver import test_driver
except:
    pass


class Solution:
    def b(self, records) -> int:
        x=(1,2e9)
        y=(1,2e9)

        for r in records:
            pass


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
        ]

        for input, res in tests[index:]:
            test_driver(s.b, input, expected=res)
