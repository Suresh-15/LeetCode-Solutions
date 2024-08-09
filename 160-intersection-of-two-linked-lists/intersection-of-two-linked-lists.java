/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) {
 * val = x;
 * next = null;
 * }
 * }
 */

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode temp1 = headA, temp2 = headB;
        int n1 = 1, n2 = 1;

        while (temp1.next != null) {
            n1 += 1;
            temp1 = temp1.next;
        }
        while (temp2.next != null) {
            n2 += 1;
            temp2 = temp2.next;
        }

        if (temp1 != temp2)
            return null;
        temp1 = headA;
        temp2 = headB;

        if (n1 > n2) {
            while (n1 != n2) {
                n1 -= 1;
                temp1 = temp1.next;
            }
        } else if (n1 < n2) {
            while (n1 != n2) {
                n2 -= 1;
                temp2 = temp2.next;
            }
        }

        while (temp1 != temp2) {
            temp1 = temp1.next;
            temp2 = temp2.next;
        }
        return temp1;
    }
}
