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
        visited = set()
        tempA, tempB = headA, headB
        while tempA or tempB:
            if tempA:
                if tempA in visited:
                    return tempA
                visited.add(tempA)
                tempA = tempA.next
            if tempB:
                if tempB in visited:
                    return tempB
                visited.add(tempB)
                tempB = tempB.next
        return None