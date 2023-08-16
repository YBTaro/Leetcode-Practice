# solution 1 - Recursive Traversal with Valid Range
# Time: O(N), since we visit each node once
# Space: O(N), for recursive
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def validate_subtree(subroot, low, high):
            if subroot is None:
                return True
            
            if subroot.val <= low or subroot.val >= high:
                return False
            
            return validate_subtree(subroot.left, low, subroot.val) and \
                   validate_subtree(subroot.right, subroot.val, high)
        return validate_subtree(root, float('-inf'), float('inf'))

# solution 2 - Iterator Traversal with Valid Range
# Time: O(N), same as previous
# Space:O(S), for stack
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            subroot, low, high = stack.pop()
            if not subroot:
                continue
            if subroot.val <= low or subroot.val>=high:
                return False
            stack.append((subroot.left, low, subroot.val))
            stack.append((subroot.right, subroot.val, high))
        return True

# Solution 3 - recursive inorder traversal
# Time: O(n)
# Space: O(n), for recursive
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev_val = float('-inf')
        def inorder(subroot):
            if not subroot:
                return True
            if not inorder(subroot.left):
                return False
            if subroot.val <= self.prev_val:
                return False
            self.prev_val = subroot.val
            return inorder(subroot.right)
        
        return inorder(root)

# solution 4 - iteration inorder traversal
# time: O(n)
# space:O(n)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True

# solution 5 - Morris Traversal (from 94. Binary Tree Inorder Traversal)
# Time: O(N), we will only get through each edge at most two times
# Space: O(1)
# Runtime: 44 ms, faster than 71.35% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.2 MB, less than 94.13% of Python3 online submissions for Validate Binary Search Tree.
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        gp = TreeNode(float('-inf'),None,root)
        now = root
        while now!= None:
            if now.left is None:
                if gp.val >= now.val:
                    return False
                gp = gp.right
                now = now.right
            else:
                left_root = now.left
                now.left = None
                left_tree_rightmost = left_root
                while left_tree_rightmost.right is not None:
                    left_tree_rightmost = left_tree_rightmost.right
                left_tree_rightmost.right = now
                now = left_root
                gp.right = now
        return True

# solution 5 - Morris Traversal
# By: https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/148939/CPP-Morris-Traversal
# Time: O(N), we will only get through each edge at most two times
# Space: O(1)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        cur = root
        prev = -math.inf

        while cur:
            if cur.left:
                left_root = cur.left
                rightmost = left_root
                while rightmost.right and rightmost.right!=cur:
                    rightmost = rightmost.right
                if rightmost.right is None:
                    rightmost.right = cur
                    cur = cur.left
                else: # second time to here, so we revert the edition we did
                    rightmost.right = None
                    if cur.val <= prev:
                        return False
                    else:
                        prev = cur.val
                        cur = cur.right
            else:
                if cur.val <= prev:
                    return False
                else:
                    prev = cur.val
                    cur = cur.right
        return True



        
            



        
            
        