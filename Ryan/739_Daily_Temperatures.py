# solution 1 - two pointer
# Time: O(n^2)
# Space: O(1)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = []
        for i in range(len(temperatures)):
            j = i+1
            while j!=len(temperatures): 
                if temperatures[i] < temperatures[j]:
                        ans.append(j-i)
                        break
                j+=1
            else:
                ans.append(0)
        return ans

# solution 2 - stack
# Time: O(n)
# Space: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return 
        ans = [0]*len(temperatures)
        stack = []
        for idx in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                past_idx = stack.pop()
                ans[past_idx] = idx - past_idx

            stack.append(idx)
        return ans