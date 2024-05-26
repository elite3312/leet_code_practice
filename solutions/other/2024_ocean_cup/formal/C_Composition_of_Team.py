# b i f
class Solution:
    
    def solve(self,diff:int,arr:list):
        res=0
        arr.sort()
        best_guy=max(arr)
        next_arr=[]
        for i in range(3):
            if arr[i]==best_guy:res+=1
            else:next_arr.append(arr[i])
        for e in next_arr:
            if abs(best_guy-e)<=diff:res+=1
        return res
        
        

if __name__ == "__main__":
    s = Solution()

    diff=int(input())
    arr=input().strip().split(' ')
    for i in range(3):
        arr[i]=int(arr[i])
    res=s.solve(diff,arr)
    print(res)
    