

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ''' 
        dominoes[i] = 'L', if the ith domino has been pushed to the left,
        dominoes[i] = 'R', if the ith domino has been pushed to the right, and
        dominoes[i] = '.', if the ith domino has not been pushed.
        '''
        dominoes=list(dominoes)
        #edge 1:single elem
        if len(dominoes)==1:return dominoes
        s=set()
        #edge 2:same dominoes for entire list
        for d in dominoes:
            s.add(d)
        if len(s)==1:
            return dominoes
        right=[0]*len(dominoes)
        left=[0]*len(dominoes)
        distance=0
        for i in range(len(dominoes)):
            if dominoes[i]=='.':
                distance+=1
            
            pass
            
        return ''.join(dominoes)
if __name__ == "__main__":

    s = Solution()
    #dominoes = "RR.L"
    dominoes = ".L.R...LR..L.."
    ans = s.pushDominoes(dominoes)
    print(ans)
