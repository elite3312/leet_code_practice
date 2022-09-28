

from cmath import inf


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ''' 
        dominoes[i] = 'L', if the ith domino has been pushed to the left,
        dominoes[i] = 'R', if the ith domino has been pushed to the right, and
        dominoes[i] = '.', if the ith domino has not been pushed.
        '''
        n=len(dominoes)
        dominoes=list(dominoes)
        #edge 1:single elem
        if len(dominoes)==1:return dominoes
        s=set()
        #edge 2:same dominoes for entire list
        for d in dominoes:
            s.add(d)
        if len(s)==1:
            return dominoes
        #otherwise
        right=[inf]*n#right[i] stands for the distance from dominoe[i] the nearest R
        
        Rs_seen=0
        for i in range(n):
            if dominoes[i]=='R':
                Rs_seen=1
            elif dominoes[i]=='.'and Rs_seen>0:
                #dominoes[i]='R'
                right[i]=Rs_seen
                Rs_seen+=1
            elif dominoes[i]=='L':
                Rs_seen=0

        left=[inf]*n#left[i] stands for the distance from dominoe[i] the nearest L
        ls_seen=0
        for i in range(n-1,-1,-1):
            if dominoes[i]=='L':
                ls_seen=1
            elif dominoes[i]=='.'and ls_seen>0:
                #dominoes[i]='R'
                left[i]=ls_seen
                ls_seen+=1
            elif dominoes[i]=='R':
                ls_seen=0
        
        for i in range(n):
            if dominoes[i]=='.':
                if right[i]>left[i]  :dominoes[i]='L'
                elif right[i]<left[i]:dominoes[i]='R'
                
        return ''.join(dominoes)
if __name__ == "__main__":

    s = Solution()
    dominoes = "RR.L"
              #"RR.L"
    #dominoes = ".L.R...LR..L.."
              #"LL.RR.LLRRLL.."
    ans = s.pushDominoes(dominoes)
    print(ans)
