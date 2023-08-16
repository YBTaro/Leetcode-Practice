# Solution 1 : brute forse - two pass
# Time: O(n)
# space: O(1)

#solution 2 : one pass
# Time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        front = head
        back = head
        
        for i in range(0,n):
            front = front.next
            
        if front == None:        # to deal with the case if we delete the head node,
            return head.next     # another solution is to add a dummy node to head.
            
        while front.next!=None:
            front, back = front.next, back.next
        
        back.next = back.next.next
        
        return head
        
        