# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode(-1,None)
        prev = start
        p1, p2 = l1, l2
        while p1 != None and p2!=None:
            if p1.val < p2.val:
                prev.next = p1
                p1 = p1.next
            else:
                prev.next = p2
                p2 = p2.next
            prev = prev.next
        if p1 == None:
            prev.next = p2
        elif p2 ==None:
            prev.next = p1
        start = start.next
        return start


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def rec(p1, p2):
            if p1==None:
                return p2
            elif p2==None:
                return p1
            
            p3 = None
            if p1.val < p2.val:
                p3 = p1
                p3.next = rec(p1.next, p2)
            else:
                p3 = p2
                p3.next = rec(p1, p2.next)
            return p3
        return rec(l1,l2)