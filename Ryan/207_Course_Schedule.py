# Solution 1 - Simple backtrack - like DFS
# Time: O(E+V^2)
# Space:O(E+V)
# overtime
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
                 
        adj_list = collections.defaultdict(list)
        visited = [0]*numCourses
        
        for pair in prerequisites:  # O(E)
            adj_list[pair[1]].append(pair[0])
        
        for course in range(numCourses): # O(V)
            if self.isCycle(course, adj_list, visited): # O(V)
                return False
        return True

    def isCycle(self, cur, adj_list, path):
        if path[cur]:
            return True # access again -> cycle
        path[cur] = 1
        for next_course in adj_list[cur]:
            if self.isCycle(next_course, adj_list, path):
                return True
        path[cur] = 0
        return False

# Solution 2 - DFS
# Time: O(E+V)
# Space: O(E+V)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
                 
        adj_list = collections.defaultdict(list)
        visited = [0]*numCourses
        checked = [0]*numCourses
        
        for pair in prerequisites:  # O(E)
            adj_list[pair[1]].append(pair[0])
        
        for course in range(numCourses): # O(V), but for each course, we only check once
            if self.isCycle(course, adj_list, visited, checked):
                return False
        return True

    def isCycle(self, cur, adj_list, path, checked):
        if path[cur]:
            return True # access again -> cycle
        if checked[cur]:
            return False # no need to check again
        path[cur] = 1
        for next_course in adj_list[cur]:
            if self.isCycle(next_course, adj_list, path, checked):
                return True
        path[cur] = 0
        checked[cur] = 1
        return False


# Solution 3 - Topological sort - Kahn's algorithm
# https://en.wikipedia.org/wiki/Topological_sorting
# Time: O(V+E)
# Space: O(V+E)

class Node:
    def __init__(self):
        self.outNodes = []
        self.inDegrees = 0
    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        Graph = collections.defaultdict(Node)
        Edges = 0
        
        for dest, src in prerequisites: # O(V)
            Graph[src].outNodes.append(dest)
            Graph[dest].inDegrees+=1
            Edges +=1
        
        # we can also use list as a stack, but for time efficient, we should use FIFO
        StartNodes = deque() 
        for idx, node in Graph.items():   # O(V)
            if node.inDegrees==0:
                StartNodes.append(idx) # append to right
        
        while StartNodes: # O(E)
            pcourse = StartNodes.pop() # pop from right
            for ncourse in Graph[pcourse].outNodes:
                Graph[ncourse].inDegrees-=1
                Edges-=1
                if Graph[ncourse].inDegrees==0:
                    StartNodes.append(ncourse)

        if Edges==0:
            return True
        else:
            return False