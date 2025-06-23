#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* removeElements(ListNode* head, int val) {

    while (head != nullptr && head->val == val)
    {
        head = head->next;
    }
    if (head == nullptr)
    {
        return nullptr;
    }

    ListNode* curr = head;
    while ( curr->next != nullptr)
    {
        if (curr->next->val == val)
        {
            curr->next = curr->next->next;
        }
        else
        {
            curr = curr->next;
        }
    }
    return head;
}

void printLL(ListNode* temp)
{
    cout << "[";
    while (temp != nullptr)
    {
        cout << temp->val << " ";
        temp = temp->next;
    }
    cout << "] ";
}

int main()
{
    ListNode* a1 = new ListNode(6);
    ListNode* a2 = new ListNode(5, a1);
    ListNode* a3 = new ListNode(4, a2);
    ListNode* a4 = new ListNode(3, a3);
    ListNode* a5 = new ListNode(6, a4);
    ListNode* a6 = new ListNode(2, a5);
    ListNode* a7 = new ListNode(1, a6);
    cout << "Removing all nodes with value of 6 resulted in a linked list "; 
    printLL(removeElements(a7, 6));
    cout << endl;

    cout << "Removing all nodes with value of 1 resulted in a linked list "; 
    printLL(removeElements(nullptr, 1));
    cout << endl;    

    ListNode* c1 = new ListNode(7);
    ListNode* c2 = new ListNode(7, c1);
    ListNode* c3 = new ListNode(7, c2);
    ListNode* c4 = new ListNode(7, c3);

    cout << "Removing all nodes with value of 7 resulted in a linked list "; 
    printLL(removeElements(c4, 7));
    cout << endl;    

    return 1;
}