# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        result = head
        while result and result.next:
            temp = result.val
            result.val = result.next.val
            result.next.val = temp
            result = result.next.next
        return head