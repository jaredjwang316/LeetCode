#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;     
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

TreeNode* sortedArrayToBST(vector<int>& nums) {
    if (nums.size() == 0)
    {
        return nullptr;
    }
    int middle = nums.size() / 2;

    vector<int> left;
    for(int i = 0; i < middle; i++)
    {
        left.push_back(nums.at(i));
    }
    
    vector<int> right;
    for(int i = middle + 1; i < nums.size(); i++)
    {
        right.push_back(nums.at(i));
    }

    TreeNode* it = new TreeNode(nums.at(middle), sortedArrayToBST(left), sortedArrayToBST(right));
    return it;
}

