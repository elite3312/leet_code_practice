class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        '''
        x can be one of the either:
        1. in arr or between some elems of arr
        2. less than the smallest elem in arr
        3. greater than the smallest elem in arr

        depending on these cases, we sample k nearest elems from arr
        '''
        n = len(arr)
        if x < arr[0]:
            # case 2
            return arr[:k]
        elif x > arr[-1]:
            # case 3
            return arr[(n-k):]
        else:
            #case 1
        
            l=[0]*n
            for i in range(n):
                l[i]=(abs(arr[i]-x),arr[i])#dist,val
            l.sort()
            #chose k nearest elems from arr
            sampled_elems=0
            res=[]
            for elem in l:
                res.append(elem[1])
                sampled_elems+=1
                if sampled_elems==k:
                    break
            res.sort()
            return res

if __name__ == "__main__":

    s = Solution()
    #arr = [1,2,3,4,5]#[1,2,3,4]
    #k = 4#find k elems
    #x = 3#target value

    #arr = [1,2,3,4,5]#[1,2,3,4]
    #k = 4
    #x = -1

    #arr = [1, 2, 3, 4, 5,6,7,8]  # [1,2,3,4]
    #k = 7
    #x = 5.5

    arr=[1,1,2,3,3,3,4,6,8,8]
    k=6
    x=1
    ans = s.findClosestElements(arr, k, x)
    print(ans)
