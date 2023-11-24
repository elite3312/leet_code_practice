
from tabulate import tabulate
class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.pages_index = 0

    def visit(self, url: str) -> None:

        # if forward pages is empty
        if self.pages_index == len(self.pages)-1:
            self.pages.append(url)
            self.pages_index = len(self.pages)-1

        # if forward pages is not empty
        elif self.pages_index < len(self.pages)-1:
            self.pages = self.pages[:self.pages_index+1]
            self.pages.append(url)
            self.pages_index = len(self.pages)-1

    def back(self, steps: int) -> str:
        dest = self.pages_index-steps
        if dest < 0:
            dest = 0
        self.pages_index = dest
        return self.pages[dest]

    def forward(self, steps: int) -> str:
        dest = self.pages_index+steps
        if dest > len(self.pages)-1:
            dest = len(self.pages)-1
        self.pages_index = dest
        return self.pages[dest]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

if __name__ == "__main__":
    s = None

    # function calls
    calls = ["BrowserHistory", "visit", "visit", "visit", "back",
             "back", "forward", "visit", "forward", "back", "back"]
    # function params
    params = [["leetcode.com"], ["google.com"], ["facebook.com"], [
        "youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2], [7]]
    # expected returns
    expected_ret = [None, None, None, None, "facebook.com", "google.com",
                    "facebook.com", None, "linkedin.com", "google.com", "leetcode.com"]
    data=[]
 
    for i in range(len(calls)):
        ret = None
        operation=None
        if calls[i] == "BrowserHistory":
            s = BrowserHistory(params[i][0])
            ret = None
            operation="init"
        elif calls[i] == "visit":
            ret = s.visit(params[i][0])
            operation="visit %s"%params[i][0]
        elif calls[i] == "back":
            ret = s.back(params[i][0])
            operation="back %d" % params[i][0]
        elif calls[i] == "forward":
            ret = s.forward(params[i][0])
            operation="forward %d" % params[i][0]
        data.append([operation,str(ret),str(expected_ret[i])])
    print(tabulate(data, headers=['operation','output', 'expected'], tablefmt='fancy_grid'))
