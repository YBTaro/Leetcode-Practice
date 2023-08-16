# solution 0 - brute force
# T(n) =  choose "(" -> T(2n-1)  + choose ")" -> T(2n-1) = 2*T(n-1)
# time: (2^(2n)) * n  (the last n is to check if each sequence is valid) 
# space: O(n) if we ignore the output size

# solution 1 - backtrack
# time: O(2^(2n)), look below -> 2021/7/11 modified, the time complexity should be leaf * tree height, and the leaf
# should be the  Catalan number (wait to be understand)
# space: O(n) for temp array
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(left = n , right = n):
            if  len(temp)==2*n:
                ans.append("".join(temp))
                return
            if left > 0:
                temp.append("(")
                backtrack(left-1, right)
                temp.pop(-1)
            if right>left:
                temp.append(")")
                backtrack(left, right-1)
                temp.pop(-1)
            
        temp = []
        ans = []
        backtrack()
        return ans
        

# The way I like to think about the runtime of backtracking algorithms is O(b^d), 
# where b is the branching factor and d is the maximum depth of recursion.

#Backtracking is characterized by a number of decisions b that can be made at each 
# level of recursion. If you visualize the recursion tree, this is the number of children 
# each internal node has. You can also think of b as standing for "base", which can help you remember that b is the base of the exponential.

#If we can make b decisions at each level of recursion, and we expand the recursion tree 
# to d levels (ie: each path has a length of d), then we get b^d nodes. Since backtracking 
# is exhaustive and must visit each one of these nodes, the runtime is O(b^d).





class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        def backtrack(stack, l,r):
            if len(stack)==2*n:
                ans.append("".join(stack))
                return
            if l>0:
                stack.append("(")
                backtrack(stack, l-1, r)
                stack.pop()
            if l<r:
                stack.append(")")
                backtrack(stack, l, r-1)
                stack.pop()

        s = []
        backtrack(s, n, n)
        return ans



class Solution:
    def isValid(self, s):
        stack = []
        table = {'(':')','{':'}','[':']'}

        for c in s:
            if c in table:
                stack.append(c)
            elif stack:
                top = stack.pop()
                if c != table[top]:
                    return False
            else:
                return False
        return not stack