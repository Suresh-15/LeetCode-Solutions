# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import math


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        if len(lists) == 0 or lists == [[]]:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            for i in lists:
                h = i
                while h:
                    l.append(h.val)
                    h = h.next
            l.sort()
            result = None
            for i in l:
                if result is None:
                    result = ListNode(i)
                    head = result
                else:
                    head.next = ListNode(i)
                    head = head.next
            return result
