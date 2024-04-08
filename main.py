from utils.test_driver import test_driver

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        i=0
        n=len(students)
        res=n
        rotate_cnt=0
        while rotate_cnt<n:
            if students[i]==sandwiches[i]:
                sandwiches.pop(0)
                students.pop(0)
                res-=1
                if len(students)==0:break
            else:
                students=students[1:]
                students.append(students[0])
                rotate_cnt+=1
        return res

        
if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                [1,1,0,0], [0,1,0,1]
            ],
            # res
            0

        ],
        [
            # inputs
            [
                [1,1,1,0,0,1], [1,0,0,0,1,1]
            ],
            # res
            3

        ],
    
    ]
    for input, res in tests:
        test_driver(s.countStudents, input[0],input[1],  expected=res)
