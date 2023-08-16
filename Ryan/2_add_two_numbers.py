# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        idx = 0
        carry = 0
        p = ans
        while (l1 is not None and l2 is not None):
            add = l1.val+l2.val+carry
            if add>9:
                carry = 1
                add = add - 10
            else:
                carry = 0
            p.next = ListNode(add)
            p = p.next
            l1 = l1.next
            l2 = l2.next
        left = l1
        if l2 is not None:
            left = l2
        while left is not None:
            add = left.val+carry
            if add>9:
                carry = 1
                add = add - 10
            else:
                carry = 0
            p.next = ListNode(add)
            p = p.next
            left = left.next
        if carry == 1:
            p.next = ListNode(carry)
        ans = ans.next
        return ans
            
            
            
            
            
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        p1,p2,pa = l1,l2,ans
        carry = 0
        while p1 is not None or p2 is not None or carry:
            if p1 is not None and p2 is not None:
                Sum = p1.val+p2.val+carry
                p1,p2 = p1.next,p2.next
            elif p1:
                Sum = p1.val+carry
                p1 = p1.next
            elif p2:
                Sum = p2.val+carry
                p2 = p2.next
            elif carry:
                Sum = carry
            carry = 0
            if Sum>9:
                Sum = Sum-10
                carry = 1
            pa.next = ListNode()
            pa = pa.next
            pa.val = Sum
        temp = ans
        ans = ans.next
        del temp
        return ans
            