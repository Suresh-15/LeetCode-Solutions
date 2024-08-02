# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        temp1, temp2, n1, n2 = headA, headB, 1, 1
        while temp1.next:
            n1 += 1
            temp1 = temp1.next
        while temp2.next:
            n2 += 1
            temp2 = temp2.next

        if temp1 != temp2:
            return None

        temp1, temp2 = headA, headB
        if n1 > n2:
            while n1 != n2:
                n1 -= 1
                temp1 = temp1.next
        elif n1 < n2:
            while n1 != n2:
                n2 -= 1
                temp2 = temp2.next

        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next

        return temp1
