/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */


class Solution {
public:
    int GCD(int a, int b) {
        if (a == 1 || b == 1)
            return 1;
        while (b != 0){
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* temp = head;
        while (temp->next != NULL) {
            int gcd = GCD(temp->val, temp->next->val);
            ListNode* mid = new ListNode(gcd, temp->next);
            temp->next = mid;
            temp = mid->next;
        }

        return head;
    }
};