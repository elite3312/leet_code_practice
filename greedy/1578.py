class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        #greedy
        n=len(colors)
        if n==1:return 0
        #find repeats, remove all except the one with largest cost
        last_seen_char='Z'
        
        res=0
        repeat_max=0
        for i in range(n):
           
            if colors[i]==last_seen_char:
                res+=neededTime[i]
                repeat_max=max(repeat_max,neededTime[i])
                if i==n-1:
                    if repeat_max!=0:
                        res-=repeat_max
            else:
                if repeat_max!=0:
                    res-=repeat_max
                repeat_max=0
                if i<=n-2 and colors[i]==colors[i+1]:
                    res+=neededTime[i]
                    repeat_max=max(repeat_max,neededTime[i])
                    
                last_seen_char=colors[i]
    

        
        return res

if __name__ == "__main__":

    s = Solution()
    #colors = "abaac"
    #neededTime = [1,2,3,4,5]#3
    #colors = "abbbcbbbb"
    #neededTime = [1,2,3,4,5,6,7,8,9]#26
    #colors = "bbbaaa"
    #neededTime = [4,9,3,8,8,9]#23
    colors = "aabaa"
    neededTime = [1,2,3,4,1]#2
    ans = s.minCost(colors,neededTime)
    print(ans)
