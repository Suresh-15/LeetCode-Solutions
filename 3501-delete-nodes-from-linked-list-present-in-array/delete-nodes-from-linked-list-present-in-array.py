# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:

        s = set(nums)
        while head:
            if head.val not in s:
                break
            head = head.next
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        while curr:
            if curr.val not in s:
                prev.next = curr
                prev = curr
            curr = curr.next
        prev.next = curr
        return head
