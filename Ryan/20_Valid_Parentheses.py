# Solution 1 - stack
# Time:O(n)
# Space:O(left)
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        left = ['(','{','[']
        right = [')','}',']']
        
        for sym in s:
            if sym in left:
                stack.append(sym)
                continue
            if not stack:
                return False
            for idx, r in enumerate(right):
                if sym==r:
                    top = stack.pop()
                    if top!=left[idx]:
                        return False
                    break
        if not stack:
            return True
        else:
            return False

# solution 1 - official solution
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
            
        