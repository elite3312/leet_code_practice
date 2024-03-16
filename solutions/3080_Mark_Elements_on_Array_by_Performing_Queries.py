from utils.test_driver import test_driver

class Solution:
    def unmarkedSumArray(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n=len(nums)
        val_and_index=[]
        i=0

        nums_sum=0
        marked=[]
        for num in nums:
            val_and_index.append((num,i))
            nums_sum+=num
            marked.append(False)
            i+=1

        
        val_and_index.sort()


        res=[]
        cur=0#for accessing val_index that is unmarked
        for q in queries:
            q_index=q[0]

            #mark index[q_index]
            if not marked[q_index]:
                marked[q_index]=True
                nums_sum-=nums[q_index]

            k=q[1]
            #mark k smallest unmarked elems
            marked_k=0
            while 1:
                if marked_k==k or cur>(n-1):break

                #if val_and_index[cur] is not marked
                if marked[val_and_index[cur][1]]==False:
                    marked[val_and_index[cur][1]]=True
                    nums_sum-=val_and_index[cur][0]
                    marked_k+=1
                cur+=1
            res.append(nums_sum)

        return res




        
if __name__ == "__main__":
    s = Solution()
    
    tests = [
        [
            # inputs
            [
                [1,2,2,1,2,3,1],[[1,2],[3,3],[4,2]]
            ],
            # res
             [8,3,0]

        ],
        [
            # inputs
            [
                [1,4,2,3],[[0,1]]
            ],
            # res
             [7]

        ],
    ]
    for input, res in tests:
        test_driver(s.unmarkedSumArray, input[0],input[1],  expected=res)
