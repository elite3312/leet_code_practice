from utils.test_driver import test_driver


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        if words == ['']:
            return ''
        d = {}  # d[a]=b means a>b

        pre_word = words[0]
        for w in words[1:]:

            curr_high = w[0]
            if pre_word[0] != curr_high:
                d[pre_word[0]] = curr_high
            else:
                index = 0
                while 1:
                    if index >= len(pre_word) or index >= len(w):
                        break

                    elif w[index] != pre_word[index]:
                        d[pre_word[index]] = w[index]
                        break
                    index += 1
            pre_word = w
        res = ""
        curr_char = words[0][0]
        while 1:
            if d.get(curr_char) == None:
                res += curr_char
                break
            res += curr_char
            curr_char = d[curr_char]
        return res


if __name__ == "__main__":
    s = Solution()

    inp = [
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]
    out = "wertf"
    # idea : lexicographic order is like giving character weights.

    # in this case, we know :
    # t > f, by looking at the 1st 2 rows(rule 1)
    # w > e, since w appeared before e(rule 2)
    # r > t, by looking at the 3rd and 4th rows
    # e > r  since e appeared before r
    # sol: iterate thru words, and use rule1 and rule2 to derive comparison relations
    
    test_driver(s.alienOrder, inp, expected=out)

    inp = [
        "z", "x"
    ]
    out = "zx"
    test_driver(s.alienOrder, inp, expected=out)

    inp = [
        ""
    ]
    out = ""
    test_driver(s.alienOrder, inp, expected=out)

    inp = [
        "11",
        "13",
        "17",
        "19",
        "2",
        "23",
        "29",
        "3",
        "5",
        "7"
    ]
    out = "123579"
    test_driver(s.alienOrder, inp, expected=out)
