# solution 1 - recursive
# Time: O(n)
# Space: O(n)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def rec(p1, p2):
            if p1==p2: # only when both of them are None
                return True
            elif p1 is None or p2 is None:
                return False
            elif p1.val != p2.val:
                return False
            return rec(p1.left, p2.right) and rec(p1.right, p2.left)
        
        return rec(root.left, root.right)


# solution 2 - stack
# Time: O(n)
# Space:O(n)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root.left, root.right)]
        while stack:
            p1, p2 = stack.pop()
            if p1==p2==None:
                continue
            elif p1 is None or p2 is None:
                return False
            elif p1.val!=p2.val:
                return False
            stack.append((p1.left, p2.right))
            stack.append((p1.right, p2.left))
        return True

