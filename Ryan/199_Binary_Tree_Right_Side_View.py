# Solution 1
# similiar as leetcode 102 Binary tree level order traversal
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        q = []
        if root is not None:
            q.append(root)
        while q:
            node = None
            level_len = len(q)
            for i in range(0,len(q)):
                node = q.pop(0)
                if i == level_len-1:
                    ans.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return ans
            
                
                
                
            
        