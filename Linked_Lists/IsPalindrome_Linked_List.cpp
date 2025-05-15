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