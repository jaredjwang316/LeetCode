#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

ListNode* reverseList(ListNode* head) {
    ListNode* curr = head;
    ListNode* prev = nullptr;

    while(curr != nullptr)
    {
        ListNode* temp = curr->next;
        curr->next = prev;

        prev = curr;
        curr = temp;
    }
    return prev;
}

