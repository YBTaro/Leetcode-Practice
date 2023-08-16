# Solution 1: dfs
# Time: O(N)
# Space: O(Tree high)
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {e.id: e for e in employees}
        
        def dfs_add(ID) -> int:
            return dic[ID].importance + sum([dfs_add(i) for i in dic[ID].subordinates])
        
        return dfs_add(id)
        