try :from utils.test_driver import test_driver
except: pass


class Solution:
    def __init__(self) -> None:
        d={}
        d['Tetrapod']=[10000,6000,3000]
        d['Longgang']=[6000,3000,2000]
        self.d=d
    def getPrize(self, group: str, place:int) -> int:
        try:
            res=self.d[group][place-1]
        except :res=0
        return res
if __name__ == "__main__":
    s = Solution()
    index=0
    submit=True
    if submit:
        group=input().strip()
        place=int(input())
        print(s.getPrize(group,place))
    else:
        group = "Longgang"
        place=2
        res=3000
        tests = [
            [
                # inputs
                [
                group,place
                ],
                # res
                res
            ],
        
            
        ]
        for input, res in tests[index:]:
            test_driver(s.getPrize, input[0],input[1] ,  expected=res)
