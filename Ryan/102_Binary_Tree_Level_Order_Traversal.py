#solution 1
# BFS traversal by queue
# time: O(n)
# space: O(n)
# In Python using Queue structure would be an overkill since 
# it's designed for a safe exchange between multiple threads and 
# hence requires locking which leads to a performance loose. 
# In Python the queue implementation with a fast atomic 
# append() and popleft() is deque.
import queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = [] 
        q = queue.Queue()
        if root is not None:
            q.put(root)
        while not q.empty():
            level_nodes = []
            for i in range(0,q.qsize()):
                node = q.get()
                level_nodes.append(node.val)
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            ans.append(level_nodes)
        return ans
            

#solution 2
# BFS traversal by list (better performance than queue)
# time: O(n)
# space: O(n) 
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = [] 
        q = []
        if root is not None:
            q.append(root)
        while q:   # means q.empty()
            level_nodes = []
            for i in range(0,len(q)):
                node = q.pop(0)
                level_nodes.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            ans.append(level_nodes)
        return ans