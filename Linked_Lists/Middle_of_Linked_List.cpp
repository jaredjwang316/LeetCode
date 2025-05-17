#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

ListNode* middleNode(ListNode* head) {
    ListNode* curr = head;
    int count = 0;
    while(curr != nullptr)
    {
        count++;
        curr = curr->next;
    }

    curr = head;
    int count_again = 0;
    while(curr != nullptr)
    {
        if(count_again == count/2 )
            return curr;
        
        count_again += 1;
        curr = curr->next;
    }
    return nullptr;
}

int main()
{
    ListNode* node1 = new ListNode(5);
    ListNode* node2 = new ListNode(4, node1);
    ListNode* node3 = new ListNode(3, node2);
    ListNode* node4 = new ListNode(2, node3);
    ListNode* node5 = new ListNode(1, node4); 
    
    cout << "The Middle Node of this Linked List has value of: " << middleNode(node5)->val << endl;

    ListNode* n1 = new ListNode(6);
    ListNode* n2 = new ListNode(5, n1);
    ListNode* n3 = new ListNode(4, n2);
    ListNode* n4 = new ListNode(3, n3);
    ListNode* n5 = new ListNode(2, n4); 
    ListNode* n6 = new ListNode(1, n5);
    
    cout << "The Middle Node of this Linked List has value of: " << middleNode(n6)->val << endl;    
    return 0;
}