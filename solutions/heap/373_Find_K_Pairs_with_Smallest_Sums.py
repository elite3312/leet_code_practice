import heapq
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        seen_pairs=set()# a pair is (nums1_index,nums2_index)
        
        my_heap=[]
        res=[]
  
        my_heap.append((nums1[0]+nums2[0],(0,0)))
        seen_pairs.add((0,0))
        while 1 :
            curr=heapq.heappop(my_heap)
            curr_pair=curr[1]
            res.append((nums1[curr_pair[0]],nums2[curr_pair[1]]))
            if  len(res)>=k:break
            
            if (curr_pair[0]+1,curr_pair[1])not in seen_pairs and curr_pair[0]+1<len(nums1):

                
                heapq.heappush(my_heap,(nums1[curr_pair[0]+1]+nums2[curr_pair[1]],
                                                (curr_pair[0]+1,curr_pair[1])))
                seen_pairs.add((curr_pair[0]+1,curr_pair[1]))
            if (curr_pair[0],curr_pair[1]+1)not in seen_pairs and curr_pair[1]+1<len(nums2):
                heapq.heappush(my_heap,(nums1[curr_pair[0]]+nums2[curr_pair[1]+1],
                                                (curr_pair[0],curr_pair[1]+1)))
                seen_pairs.add((curr_pair[0],curr_pair[1]+1))
            if len(my_heap)==0:break
        return res
            
        
def test_driver(s: Solution, input1: any, input2: any,input3: any, expected: str):
    # change this line
    ans = s.kSmallestPairs(input1,input2,input3)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)



if __name__ == "__main__":

    s = Solution()
    
    test_driver(s,[1,7,11],[2,4,6],4,[[1,2],[1,4],[1,6],[2,7]])
    test_driver(s,[1,7,11],[2,4,6],3,[[1,2],[1,4],[1,6]])
    test_driver(s,[1,1,2],[1,2,3],2,[[[1,1],[1,1]]])
    test_driver(s,[1,2],[3],3,[[[1,3],[2,3]]])

    
