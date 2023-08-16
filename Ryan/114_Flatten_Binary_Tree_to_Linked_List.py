# solution 1: recursive
# Time: O(n)
# Space: O(n) for recursive
# Step:
#    1. if right subtree exists: flatten right subtree
#    2. if left subtree exists: flatten left subtree, and modify the pointer to flattten the tree
#    3. return right most grand-child
#    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:
    def flatten(self, root: TreeNode) -> None:    
        if not root:
            return
        
        def flat_subtree(subroot) -> TreeNode: # reture right most node of this subtree
            if subroot.right:
                flat_subtree(subroot.right)
                
            if subroot.left:
                left_rightmost = flat_subtree(subroot.left)
                left_rightmost.right = subroot.right
                subroot.right = subroot.left
                subroot.left = None
                
            rightmost = subroot
            while rightmost.right:
                rightmost = rightmost.right
            return rightmost
        flat_subtree(root)
        return 
                
# Solution 2 - stack - official
# Time: O(N)
# Space: O(N)
# In the first solution, we rely on the system stack for our recursion's space requirements. 
# However, as we all know, that stack is limited and for extremely long trees, it might not 
# be feasible to use the system stack. So, we need to use our own stack that will be allocated 
# memory on the heap and will be able to handle much larger sized trees easily.

import collections
class Solution:
    def flatten(self, root: TreeNode) -> None:    
        if not root:
            return None
        
        START, END = 1, 2
        
        tailNode = None
        stack = [[root, START]]
        
        while stack:
            currentNode, recursionState = stack.pop()
            
            if not currentNode.left and not currentNode.right:
                tailNode = currentNode
                continue
            
            # If the node is in the START state, it means we still
            # haven't processed it's left child yet.
            if recursionState == START:
                if currentNode.left: 
                    stack.append((currentNode, END))         
                    stack.append((currentNode.left, START))
                else:
                    stack.append((currentNode.right, START))
            else: # if recursionState == END, means we finish the flatting of left subtree. (the left subtree mush exist)
                rightNode = currentNode.right
                
                if tailNode: # Since we update tailNode when we access any tails, so it must be the previous order if this root
                    tailNode.right = currentNode.right
                    currentNode.right = currentNode.left
                    currentNode.left = None
                    rightNode = tailNode.right
                
                if rightNode:
                    stack.append((rightNode, START))                

# Solution 2 - stack - someone provide, easily understood
# Time: O(n)
# Space: O(n)
class Solution:
    def flatten(self, root: TreeNode) -> None:
       
        if not root:
            return
    
        stack = [root]
        prev = None
        
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                if prev:
                    prev.right = node
                    prev.left = None 
                prev = node

# Solution 3 - modify pointer directly
# Time: O(n)
# Space: O(1)
class Solution:
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                left_rightmost = cur.left
                while left_rightmost.right:
                    left_rightmost = left_rightmost.right
                left_rightmost.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
        return
        
        