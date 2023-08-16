# Solution 1 - stack
# Time: O(N)
# Space: O(N)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if abs(a) < stack[-1]:
                    break
                elif a==-stack.pop():
                    break
            else:
                stack.append(a)
        return stack