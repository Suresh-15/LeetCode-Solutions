# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummyHead = ListNode(-1, head)
        curr = dummyHead

        while curr and curr.next and curr.next.next:
            nextNode = curr.next
            curr.next = curr.next.next
            curr = curr.next
            tempNodes = curr.next
            curr.next = nextNode
            curr = curr.next
            curr.next = tempNodes
        
        return dummyHead.next