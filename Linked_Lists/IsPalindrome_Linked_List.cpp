#include <iostream>
#include <vector>
using namespace std;

/**
 * Definition for singly-linked list. */
 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

bool isPalindrome(ListNode* head) {
    vector<int> nodeVals;
    ListNode* curr = head;
    while(curr != nullptr)
    {
        nodeVals.push_back(curr->val);
        curr = curr->next;
    }

    int left = 0;
    int right = nodeVals.size() - 1;
    while(left < right)
    {
        if (nodeVals.at(left) != nodeVals.at(right))
            return false;
        left += 1;
        right -= 1;
    }
    return true;
}

int main() {
    // Create the linked list: 1 -> 2 -> 2 -> 1
    ListNode* node4 = new ListNode(1);
    ListNode* node3 = new ListNode(2, node4);
    ListNode* node2 = new ListNode(2, node3);
    ListNode* node1 = new ListNode(1, node2);
    ListNode* head = node1;

    // Test isPalindrome
    if (isPalindrome(head)) {
        cout << "The linked list is a palindrome." << endl;
    } else {
        cout << "The linked list is not a palindrome." << endl;
    }

    // Clean up memory
    delete node1;
    delete node2;
    delete node3;
    delete node4;

    // ---- Test Case 2: Not a Palindrome ----
    ListNode* m3 = new ListNode(3);
    ListNode* m2 = new ListNode(2, m3);
    ListNode* m1 = new ListNode(1, m2);
    ListNode* head2 = m1;

    if (isPalindrome(head2)) {
        cout << "Test 2: The linked list is a palindrome." << endl;
    } else {
        cout << "Test 2: The linked list is not a palindrome." << endl;
    }

    // Clean up memory
    delete m1; 
    delete m2; 
    delete m3;
    
    return 0;
}