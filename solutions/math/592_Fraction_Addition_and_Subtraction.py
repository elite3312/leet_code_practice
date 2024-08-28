from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
import math


#def lcm_using_gcd(a, b):
#    gcd = math.gcd(a, b)
#    lcm = (a * b) // gcd
#    return lcm


class Solution:
    def fractionAddition(self, expression: str) -> str:

        first = True  # for processing the first number

        if expression[0] != '-':
            cur_sign = 1
        else:
            expression = expression[1:]
            cur_sign = -1

        cur_num = []

        def inner():
            '''find lcm of 'cur_denom' and 'denom', redcuces to common denom,
            performs addition and then converts to irreducible fraction
            '''
            nonlocal cur_denom, denom, numer, cur_numer, cur_sign
            lcm = math.lcm(cur_denom, denom)

            # 通分
            numer *= int(lcm/denom)
            cur_numer *= int(lcm/cur_denom)
            numer += cur_sign*cur_numer
            denom = lcm

            # 化簡
            if numer == 0:
                denom = 1
            else:
                gcd = math.gcd(numer, denom)
                numer = int(numer/gcd)
                denom = int(denom/gcd)

        for c in expression:
            if c == '/':
                if first:
                    numer = cur_sign * int(''.join(cur_num))
                else:
                    cur_numer = int(''.join(cur_num))
                cur_num.clear()
            elif c in ['+', '-']:

                if first:
                    denom = int(''.join(cur_num))
                    first = False
                else:
                    cur_denom = int(''.join(cur_num))
                    inner()

                cur_num.clear()
                if c != '-':
                    cur_sign = 1
                else:
                    cur_sign = -1

            else:
                cur_num.append(c)

        # process last number, since inner() does not trigger in the last iteration
        if first:
            denom = int(''.join(cur_num))
        else:
            cur_denom = int(''.join(cur_num))
            inner()

        res = []

        res.append(str(numer))
        res.append('/')
        res.append(str(denom))
        res = ''.join(res)
        return res


if __name__ == "__main__":

    sol = Solution()

    index = 0

    tests = [
        [["-1/2+1/2"], "0/1"],
        [
            ["-1/2+1/2+1/3"], "1/3"
        ],
        [
            ["1/3-1/2"], "-1/6"
        ],
        [
            ["3/5-6/7"], "-9/35"
        ],
        [
            ["7/2+2/3-3/4"],"41/12"
            # 7/2+2/3=21+4/6=25/6
            # 25/6-3/4=50/12-9/12=41/12
            
        ]
    ]

    test_driver_main(sol.fractionAddition, tests, index)
