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
    bool isPalindrome(ListNode* head) {
        ListNode* temp1 = head;
        int length = 0;
        while (temp1 != nullptr) {
            length++;
            temp1 = temp1->next;
        }

        ListNode *temp, *prev = nullptr;
        ListNode* temp2 = head;
        temp1 = head;
        while (temp2 != nullptr && temp2->next != nullptr) {
            temp1 = temp1->next;
            temp2 = temp2->next->next;
        }
        while (head != temp1) {
            temp = head->next;
            head->next = prev;
            prev = head;
            head = temp;
        }
        if (length % 2 == 1)
            temp1 = temp1->next;
        temp2 = temp1;
        while (prev != temp1 && temp2 != nullptr) {
            if (prev->val == temp1->val) {
                prev = prev->next;
                temp1 = temp1->next;
            } else
                return false;
        }
        return true;
    }
};