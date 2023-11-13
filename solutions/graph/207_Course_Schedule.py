from collections import defaultdict
class Solution_v0:
    # idea: iterate thru courses, each pass check if prereqs are met, gradually complete all courses. faster than 5%.
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if numCourses==1 :
            if prerequisites==None:return True
        
        d=defaultdict(list)# haspmap for prereqs
        for p in prerequisites:
            d[p[0]].append(p[1])

        finished=[0 for _ in range(numCourses)]
        last_finished_num=None
        res=None
        while 1:
            not_all_done=False
            finished_num=0
            for c in range(numCourses):
                if finished[c]:
                    finished_num+=1
                    continue
                if len(d[c])==0:
                    finished_num+=1
                    # can finish course c
                    finished[c]=1
                else:
                    prereq_not_done=False
                    for prereq in d[c]:
                        if finished[prereq]==0:
                            prereq_not_done=True
                            break
                    if prereq_not_done==False:
                        finished_num+=1
                        finished[c]=1
                if finished[c]==0:
                    not_all_done=True
            if not_all_done==False:
                res=True
                break
            if last_finished_num==finished_num:
                res=False
                break
            last_finished_num=finished_num
        return res
class Solution_v1:
    # idea: same as v0, but slightly faster 
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if prerequisites==None or len(prerequisites)==0:return True
        
        prereqs=defaultdict(list)# haspmap for prereqs
        for p in prerequisites:
            prereqs[p[0]].append(p[1])

        finished=[0 for _ in range(numCourses) ]# haspmap for course completion
        not_finished=[]
        for c in range(numCourses):
            if len(prereqs[c])>=1:
                not_finished.append(c)
            else:finished[c]=1

        not_finished_next=[]# we need this to jump to next iteration
        while 1:
            for c in not_finished:
                prereq_not_done=False
                for prereq in prereqs[c]:
                    if finished[prereq]==0:
                        prereq_not_done=True
                        not_finished_next.append(c)
                        break
                if prereq_not_done==False:# this means all prereqs are met
                    finished[c]=1
            
            if len(not_finished_next)==len(not_finished):return False
            elif len(not_finished_next)==0:return True
            not_finished=not_finished_next
            not_finished_next=[]
from collections import deque    
class Solution:
    # kahn's algorithm
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for x in range(numCourses)]
        
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = 0
        while len(queue)>0:
            node = queue.popleft()
            visited += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return numCourses == visited
                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()
    numCourses = 4
    prerequisites = [[2,0],[1,0],[3,1],[3,2],[1,3]]
    test_driver(s.canFinish,numCourses,prerequisites,expected=False)
    numCourses = 2
    prerequisites = [[1,0]]
    test_driver(s.canFinish,numCourses,prerequisites,expected=True)
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    test_driver(s.canFinish,numCourses,prerequisites,expected=False)
    numCourses = 1
    prerequisites = []
    test_driver(s.canFinish,numCourses,prerequisites,expected=True)