# solution 1 - DFS
# Time: O(n^2), since we travel through the N*N adj matrix
# Space: O(n)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(i):
            visited[i] = 1
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1 and visited[j]==0:
                    dfs(j)
        
        cnt = 0
        visited = [0] * len(isConnected)
        for i in range(len(isConnected)):
            if visited[i]==0:
                cnt+=1
                dfs(i)
        return cnt

# solution 2 - BFS
# TIme: O(n^2)
# Space: O(n)