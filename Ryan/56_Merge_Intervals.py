# solution 1 - build component then merge - practice tuple and list skill
# 1. build graph
# 2. merge component
# 3. get min, max for each component

# Time: O(N^2) for BuildGraph
# Space: O(N^2) for Graph (all interval overlap with all other iterval)
# Time Limit Exceeded in LeetCode
class Solution:       
    def BuildGraph(self, intervals): # O(N^2)
        def overlap(a:list, b:list):
            return ((a[0] <= b[1]) and (b[0] <= a[1]))
        graph = collections.defaultdict(list)
        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)
        return graph
    
    def GetComponemts(self, graph, intervals): # O(N)
        
        visited =set()
        components = collections.defaultdict(list)
        component_num = 0
        
        def DFS_Component(startnode):
            stack = [startnode]
            while stack:
                interval = stack.pop()
                if tuple(interval) in visited:
                    continue
                visited.add(tuple(interval))
                components[component_num].append(interval)
                stack.extend(graph[tuple(interval)])
        
        for interval in intervals:
            if tuple(interval) not in visited:
                DFS_Component(interval)
                component_num+=1
        return components, component_num
    
    def mergecomponent(self, intervals): # O(N)
        min_start = min([interval[0] for interval in intervals])
        max_end = max([interval[1] for interval in intervals])
        return [min_start, max_end]
                
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.BuildGraph(intervals)
        components, component_num = self.GetComponemts(graph, intervals)
        return [self.mergecomponent(components[idx]) for idx in range(component_num)]

# solution 2 - sort and greedt
# Time: O(nlogn)
# Space: O(n) for sort (if we use bubble or selection sort, it should be O(1), but the time will be O(n^2))
# Runtime: 76 ms, faster than 97.79% of Python3 online submissions for Merge Intervals.
# Memory Usage: 16.1 MB, less than 83.69% of Python3 online submissions for Merge Intervals.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0] )
        
        ans = [ intervals[0] ]
        for i in range(1, len(intervals)):
            if ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans