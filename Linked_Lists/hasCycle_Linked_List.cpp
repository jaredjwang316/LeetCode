#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
 };

bool hasCycle(ListNode *head) {
    //Use Floyd and Tortoise Hare Algorithm
    if (head == nullptr || head->next == nullptr)
        return false;
    ListNode* slow = head;
    ListNode* fast = head->next;
    while (fast != slow)
    {
        if (fast == nullptr || fast->next == nullptr)
        {
            return false;
        }
        slow = slow->next;
        fast = fast->next->next;
    }
    return true;
}

int main()
{
    ListNode* a4 = new ListNode(-4);
    ListNode* a3 = new ListNode(0);
    a3->next = a4;
    ListNode* a2 = new ListNode(2);
    a2->next = a3;    
    ListNode* a1 = new ListNode(3);
    a1->next = a2;  
    a4->next = a2; 
    cout << "This Singly Linked List has a cycle: " << hasCycle(a1) << endl;
    return 0;
}