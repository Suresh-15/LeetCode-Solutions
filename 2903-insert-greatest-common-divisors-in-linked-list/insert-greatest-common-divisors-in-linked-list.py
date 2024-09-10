# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:

        def GCD(a, b):
            while b:
                a, b = b, a % b
            return a


        temp = head
        while temp.next:
            gcd = GCD(temp.val, temp.next.val)
            mid = ListNode(gcd, temp.next)
            temp.next = mid
            temp = mid.next

        return head