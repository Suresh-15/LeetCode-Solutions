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
    ListNode* reverseList(ListNode* head) {
        ListNode *reverse = NULL;
        ListNode *current = head;
        while(current != NULL) {
            ListNode *next = current->next;
            current->next = reverse;
            reverse = current;
            current = next;
        }
        return reverse;
    }
    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* reverse = reverseList(slow->next);
        slow->next = NULL;
        while (reverse != NULL) {
            if (head->val != reverse->val) {
                return false;
            }
            head = head->next;
            reverse = reverse->next;
        }
        return true;
    }
};