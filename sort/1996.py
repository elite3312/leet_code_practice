
class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        #properties.sort(reverse=True)
        max_0=properties[0][0]
        max_1=properties[0][1]
        res=0
        first=True
        for elem in properties:
            if first:
                first=False
                continue
            if elem[0]<max_0 and elem[1]<max_1:
                res+=1
            else:
                max_0=elem[0]
                max_1=elem[1]
            print(elem)
            


        return res
        
if __name__ == "__main__":
    
    s = Solution()
    #properties = [[5,5],[6,3],[3,6]]
    #properties = [[1,20],[2,10],[3,30]]
    properties=[[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]#2
    #properties=[[1,1],[2,1],[2,2],[1,2]] #1
    ans=s.numberOfWeakCharacters(properties)
    print(ans)
    