
# 1. remove elems from cost where costs[i][0]==costs[i][1]
# 2. sort the updated costs by key=lambda x:abs(x[0]-x[1])
# 3. iterate thru the sorted costs, take min (costs[i][0],costs[i][1]), also record the number of "a"s and "b"s taken. 
#If either number of "a"s or "b"s taken reaches n, only take from the other set.
class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        n=len(costs)//2
        filtered_cost=[]
        res=0
        for c in costs:
            if c[0]==c[1]:
                res+=c[0]
            else:
                filtered_cost.append(c)
        filtered_cost.sort(key=lambda x:abs(x[0]-x[1]),reverse=True)

        
        a_count=0
        b_count=0
        for i in range(len(filtered_cost)):
            a_cost=filtered_cost[i][0]
            b_cost=filtered_cost[i][1]
            if a_count==n:
                res+=b_cost
            elif b_count==n:
                res+=a_cost
            
            else:
                
                if a_cost<b_cost:
                    res+=a_cost
                    a_count+=1
                elif a_cost>b_cost: 
                    res+=b_cost
                    b_count+=1
                else:
                    raise Exception("!")
        return res
    






        
if __name__ == "__main__":
    s=Solution()
    
    

    input1=[[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    #
    expected=1859
    print(s.twoCitySchedCost(input1),' ans=',expected) 

    input1=[[10,20],[30,200],[400,50],[30,20]]
    #aabb
    expected=110
    print(s.twoCitySchedCost(input1),' ans=',expected) 