class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        graph = {i: [] for i in range(numCourses)}
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        def dfs(course, visiting):
            if course in visiting:
                return False
            
            visiting.add(course)
            
            for pre in graph[course]:
                if not dfs(pre, visiting):
                    return False
            
            visiting.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        
        return True