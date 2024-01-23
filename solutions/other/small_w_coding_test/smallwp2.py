from utils.test_driver import test_driver

class Solution:
    def cell_state(self,cell:list,days:int):
        n=len(cell)
        for _ in range(days):
            cur=[None for _ in cell]
            for i,c in enumerate(cell):
                if(i==0):
                    if cell[1]==0:cur[i]=0
                    else :cur[i]=1
                elif(i==n-1):
                    if cell[n-2]==0:cur[i]=0
                    else :cur[i]=1
                else:
                    if cell[i-1]==cell[i+1]:cur[i]=0
                    else :cur[i]=1
            cell=cur
        return cell

                    
        

if __name__ == "__main__":
    s = Solution()
 

    tests = [
            [#case 1
            # input
            [
                [1 if x =='1' else 0 for x in "11101111"],1
            ],
            #res
            [1 if x =='1' else 0 for x in "10101001"]
         
            ],
            [#case 2
            # input
            [
                [1 if x =='1' else 0 for x in "11101111"],2
            ],
            #res
            [1 if x =='1' else 0 for x in "00000110"],
        
            ],
         
        ]
    for input, res in tests:
        test_driver(s.cell_state, input[0], input[1],expected=res)
