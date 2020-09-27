# https://leetcode.com/problems/course-schedule-ii/submissions/

class Solution(object):
    
    def DepthFirstSearch(self, current, visited, currentSet, ans, prereq):
        
            currentSet.add(current)
            
            if current in prereq:
                for course in prereq[current]:
                    
                    if course in visited:
                        continue

                    if course in currentSet:
                        return False

                    if not self.DepthFirstSearch(course, visited, currentSet, ans, prereq):
                        return False
            
            currentSet.remove(current)
            visited.add(current)
            
            ans.append(current)
            
            return ans
            
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq = {}
        
        for prerequisit in prerequisites:
            
            if prerequisit[0] in prereq:
                prereq[prerequisit[0]].append(prerequisit[1])
                
            else:
                prereq[prerequisit[0]] = [prerequisit[1]]
            
        visited = set()
        ans = []
        
        for course in range(numCourses):

            if course in visited:
                continue
            
            if not self.DepthFirstSearch(course, visited, set(), ans, prereq):
                return []
            
        return ans