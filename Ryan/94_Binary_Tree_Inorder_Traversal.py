# Solution 1 - recursive
# time:O(n)
# space: O(n) in worst case, but O(log n ) in average
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if root is None:
            return ans
        ans = ans + self.inorderTraversal(root.left)
        ans.append(root.val)
        ans = ans + self.inorderTraversal(root.right)
        return ans

# Solution 2 - Morris Traversal - first version
# current pointer starts from root, if current.left exist, do rotation
# How to rotation?
# A:use current.left_subtree to replace current, and paste the current amd its right subtree to the rightmost node.right of the original curremt.left_subtree
# if current.left not exist, current = current.right, check again.
# keep doing the check until the whole nodes only have right child
# time:O(n), Intuitively, the complexity is O(nlogn), because to
#      find the predecessor node for a single node related to the
#      height of the tree. But in fact, finding the predecessor nodes 
#      for all nodes only needs O(n) time. Because a binary Tree 
#      with n nodes has n-1 edges, the whole processing for each 
#      edges up to 2 times, one is to locate a node, and the other is to 
#      find the predecessor node. So the complexity is O(n)O(n).
# space:O(1) or O (n)??
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        current = root
        gp = TreeNode(0,None,current)
        while current is not None:
            if current.left is None:
                ans.append(current.val)
                gp=gp.right
                current = current.right
            else:
                subtree_root = current.left
                current.left = None
                gp.right = subtree_root
                rightmost = subtree_root
                while rightmost.right is not None:
                    rightmost = rightmost.right
                rightmost.right = current
                current = subtree_root
        return ans

# Solution 2 - Morris Traversal - second version
# https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/148939/CPP-Morris-Traversal
# Time:O(N)
# Space:O(1)

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        current = root
        while current:
            if current.left:
                left_root = current.left
                rightmost = left_root
                while rightmost.right and rightmost.right!=current:
                    rightmost = rightmost.right
                if rightmost.right is None:
                    rightmost.right = current
                    current = current.left
                else: # second time to here, so we revert the edition we did
                    rightmost.right = None
                    ans.append(current.val)
                    current = current.right
            else:
                ans.append(current.val)
                current = current.right
        return ans

"""
1. Initialize current as root 
2. While current is not NULL
   If current hs a left child
      ifa) Make current as right child of the rightmost 
         node in current's left subtree
      ifb) Go to this left child, i.e., current = current->left
   Else
      ea) Print current’s data
      eb) Go to the right, i.e., current = current->right
"""