# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        cur1, cur2, n1, n2 = headA, headB, 1, 1
        while cur1.next:
            n1 += 1
            cur1 = cur1.next
        while cur2.next:
            n2 += 1
            cur2 = cur2.next

        if cur1 != cur2:
            return None

        cur1, cur2 = headA, headB
        if n1 > n2:
            while n1 != n2:
                n1 -= 1
                cur1 = cur1.next
        elif n1 < n2:
            while n1 != n2:
                n2 -= 1
                cur2 = cur2.next

        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next

        return cur1
