# Solution 1 - DFS
# Time: O(E+V)
# Space: O(E+V)
# Runtime: 88 ms, faster than 98.62% of Python3 online submissions for Course Schedule II.
# Memory Usage: 16.8 MB, less than 37.89% of Python3 online submissions for Course Schedule II.
class Solution:
    def dfs(self, course, adj_list, visited, checked, output):
        if visited[course]:
            return False # impossible
        if checked[course]:
            return True # it's fine
        visited[course] = 1
        
        for ncourse in adj_list[course]:
            if not self.dfs(ncourse, adj_list, visited, checked, output):
                return False
        visited[course] = 0
        checked[course] = 1
        output.append(course)
        return True
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = collections.defaultdict(list)
        visited = [0] * numCourses
        checked = [0] * numCourses
        
        for dest, res in prerequisites: # O(E)
            adj_list[res].append(dest)
        
        output = collections.deque()
        
        for course in range(numCourses): # O(V)
            if not self.dfs(course, adj_list, visited, checked, output):
                return []
        output.reverse()
        return output
        
# Solution 1.1 - Official DFS
from collections import defaultdict
class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses, prerequisites):
        adj_list = defaultdict(list)

        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        non_cycle = True

        # By default all vertces are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal non_cycle

            if not non_cycle: 
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        non_cycle = False

            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []

# Solution 2 - Kahn's algorithm
# Time: O(E+V)
# Space: O(E+V)
class Node:
    def __init__(self):
        self.indegrees = 0
        self.outnodes = []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        Nodes = collections.defaultdict(Node)
        Edges = 0
        
        for dest, res in prerequisites: # O(E)
            Nodes[res].outnodes.append(dest)
            Nodes[dest].indegrees+=1
            Edges+=1
        
        StartNodes = collections.deque()        
        #for idx, node in Nodes.items():
        #    if node.indegrees==0:
        #        StartNodes.append(idx)
        for idx in range(numCourses):
            if Nodes[idx].indegrees==0:
                StartNodes.append(idx)
        
        output = []
        
        while StartNodes:
            course = StartNodes.pop()
            output.append(course)
            
            for ncourse in Nodes[course].outnodes:
                Nodes[ncourse].indegrees -=1
                if Nodes[ncourse].indegrees == 0:
                    StartNodes.append(ncourse)
                Edges -=1
        
        return output if Edges==0 else []

# Solution 2.1 - Official Kahn's algorithm
from collections import defaultdict, deque
class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []