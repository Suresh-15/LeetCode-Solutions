# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        result, lag = head.next, ListNode(0)
        left, right = head, head.next

        while left and left.next:
            temp = right.next
            right.next = left
            left.next = temp
            lag.next = right
            lag = left
            left = left.next
            if left:
                right = left.next
            else:
                break
            
        return result