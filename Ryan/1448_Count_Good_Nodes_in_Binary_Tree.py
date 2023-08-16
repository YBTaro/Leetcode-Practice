# Solution 1 - maxlimit as parameter
# Time: O(n)
# Space: O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
                       
        def findgood(subroot, maxlimit = -math.inf):
            a = self.ans
            if not subroot:
                return
            if subroot.val >= maxlimit:
                self.ans +=1
                a = self.ans
            maxlimit = max(maxlimit, subroot.val)
            findgood(subroot.left, maxlimit)
            findgood(subroot.right, maxlimit)
        
        self.ans = 0
        findgood(root)
        
        return self.ans