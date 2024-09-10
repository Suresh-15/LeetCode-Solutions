/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */


class Solution {
    public int GCD(int a, int b) {
        if (b == 0)
            return a;
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode temp = head;
        while (temp.next != null) {
            int gcd = GCD(temp.val, temp.next.val);
            ListNode mid = new ListNode(gcd, temp.next);
            temp.next = mid;
            temp = mid.next;
        }

        return head;
    }
}