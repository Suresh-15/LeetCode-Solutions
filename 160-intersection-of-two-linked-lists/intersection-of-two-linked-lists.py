# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        def listLen(node):
            count = 0
            while(node):
                count += 1
                node = node.next
            return count
        
        lenA = listLen(headA)
        lenB = listLen(headB)
        remaining = min(lenA, lenB)
        if lenA < lenB:
            c = lenB-lenA
            while c:
                headB = headB.next
                c = c - 1
        elif lenA > lenB:
            c = lenA-lenB
            while c:
                headA = headA.next
                c = c - 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA