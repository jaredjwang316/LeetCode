#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    if (list1 == nullptr)
        return list2;
    else if (list2 == nullptr)
        return list1;
    
    ListNode* mergedList;
    if (list1->val < list2->val)
    {
        mergedList = list1;
        mergedList->next = mergeTwoLists(list1->next, list2);
    }
    else
    {
        mergedList = list2;
        mergedList->next = mergeTwoLists(list1, list2->next);
    }

    return mergedList;
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
    ListNode* a1 = new ListNode(4);
    ListNode* a2 = new ListNode(2, a1);
    ListNode* a3 = new ListNode(1, a2);

    ListNode* b1 = new ListNode(4);
    ListNode* b2 = new ListNode(3, b1);
    ListNode* b3 = new ListNode(1, b2);

    cout << "The resulting merged list is ";
    printLL(mergeTwoLists(a3, b3));
    cout << endl;
}