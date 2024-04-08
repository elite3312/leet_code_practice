from utils.test_driver import test_driver

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        i=0
        n=len(students)
        res=n
        rotate_cnt=0
        while 1:
            if students[i]==sandwiches[i]:
                sandwiches.pop(0)
                students.pop(0)
                res-=1
                if len(students)==0:break
            else:
                head_student=students.pop(0)
                students.append(head_student)
                rotate_cnt+=1
                if rotate_cnt>=n*n:break

        return res

        
if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                [1], [1]
            ],
            # res
            0

        ],
        [
            # inputs
            [
                [1], [0]
            ],
            # res
            1

        ],
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
