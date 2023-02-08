class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        #2 <= n <= 9
        #0 <= k <= 9

        ans = {}
        for i in range(1,10):
            get_child(n, k, str(i), ans)
        return list(ans.keys())


def get_child(n: int, k: int, curr: str, res: list[int]):
    if len(curr) == n:
        res[curr] = 1
        return
    next = curr
    
    last_digit_of_next = next[-1]
    last_digit_of_next = int(last_digit_of_next)

    next_digit = int(str(last_digit_of_next+k))
    if (next_digit < 10):
            
        next = next+str(next_digit)

        get_child(n, k, next, res)
    next = curr
 
 
    last_digit_of_next = next[-1]
    last_digit_of_next = int(last_digit_of_next)

    next_digit = int(str(last_digit_of_next-k))
    if (next_digit >= 0):
            
        next = next+str(next_digit)

        get_child(n, k, next, res)


if __name__ == "__main__":
    s = Solution()
    #n = 3  # len
    #k = 4  # diff
    #
    #n=3
    #k=7
    n=2
    k=1
    print(s.numsSameConsecDiff(n, k))
