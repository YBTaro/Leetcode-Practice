# Solution 1
# bottom-up to find the max_sum of subtree, and return each child's max_sum for roots to find if there is bigger sum
# time: O(n)
# space: O(log n) --> tree height
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self, num = None):
        self.max_sum = num
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.BottomUp_Helper(root)
        return self.max_sum
    
    def BottomUp_Helper(self, root: TreeNode):
        cpr_list = [root.val] if self.max_sum is None else [root.val, self.max_sum]
        return_list = [root.val]
        left_tree, right_tree = None, None
        if root.left is None and root.right is None:
            self.max_sum = max(cpr_list)
            return root.val
        if root.left is not None:
            left_tree = self.BottomUp_Helper(root.left)
            cpr_list.append(root.val+left_tree)
            return_list.append(root.val+left_tree)
        if root.right is not None:
            right_tree = self.BottomUp_Helper(root.right)
            cpr_list.append(root.val+right_tree)
            return_list.append(root.val+right_tree)
        if root.left is not None and root.right is not None:
            cpr_list.append(root.val+left_tree+right_tree)
        cpr_list.append(self.max_sum)
        self.max_sum = max(cpr_list)
        return max(return_list)