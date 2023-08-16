# Solution 1: stack - myself 
# Time: O(n)
# Space: O(n)
# Runtime: 84 ms, faster than 93.72% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
# Memory Usage: 15.6 MB, less than 96.54% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for idx, c in enumerate(s):
            if c == '(':
                stack.append(('(',idx))
            elif c == ')':
                if stack and stack[-1][0]=='(':
                    stack.pop()
                else:
                    stack.append((')',idx))
        ans = []
        start = 0
        for _, idx in stack:
            ans.append(s[start:idx])
            start = idx+1
        if start!=len(s):
            ans.append(s[start:])
        return ''.join(ans)
        

# solution 2: balance and reverse - two pass
# Time: O(n)
# Space: O(n)

class Solution:
    def minRemoveToMakeValid(self, s:str) -> str:

        def DeleteInvaludPara(s, openpara, closepara):
            balance = 0
            sb = []
            for c in s:
                if c == closepara:
                    if balance<=0:
                        continue
                    balance-=1
                elif c == openpara:
                    balance+=1
                sb.append(c)
            return ''.join(sb)

        s = DeleteInvaludPara(s,'(',')')
        s = DeleteInvaludPara(s[::-1],')','(')
        return s[::-1]



