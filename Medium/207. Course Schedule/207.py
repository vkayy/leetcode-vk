from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {}
        
        for c, p in prerequisites:
            if c not in preMap:
                preMap[c] = []
            preMap[c].append(p)
        
        visited = set()
        
        def dfs(course):
            
            if course in visited:
                return False
            
            if preMap.get(course, []) == []:
                return True
            
            visited.add(course)
            
            if any(not dfs(prereqs) for prereqs in preMap.get(course, [])):
                return False
            
            visited.remove(course)
            preMap[course] = []
            
            return True
        
        return all(dfs(n) for n in range(numCourses))

# first, we create a map called preMap
# this will map a course to its prerequisites

# then, we iterate through the prerequisites
# if the course is not in preMap, we add it
# then, we append the prerequisite to the list of prerequisites

# then, we create a set called visited

# then, we create a function called dfs that takes in a course

# if the course is in visited, we return False
# if the course has no prerequisites, we return True

# we add the course to visited

# if any of its prequisites have cycles, then the course cannot be taken
# so, we return False

# otherwise, we remove the course as we are done validating it
# then, we set the prerequisites of the course to an empty list
# this marks that the course can be taken
# so, we return True

# then, we iterate through the courses
# if all the courses can be taken, we return True