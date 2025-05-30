#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

TreeNode* searchBST(TreeNode* root, int val) {
    if (root == nullptr) 
    {
        return nullptr;
    }
    else if (root->val == val)
    {
        return root;
    }
    else if (root->val > val)
    {
        return searchBST(root->left, val);
    }
    return searchBST(root->right, val);
}

int main()
{
    TreeNode* t1 = new TreeNode(1);
    TreeNode* t2 = new TreeNode(3);
    TreeNode* t3 = new TreeNode(2, t1, t2);
    TreeNode* t4 = new TreeNode(7);
    TreeNode* t5 = new TreeNode(4, t3, t4);

    if (searchBST(t5, 2) == nullptr)
        cout << "Node with value 2 does not exist in the tree" << endl;
    else
        cout << searchBST(t5, 2) << endl;

    if (searchBST(t5, 5) == nullptr)
        cout << "Node with value 5 does not exist in the tree" << endl;
    else
        cout << searchBST(t5, 5) << endl;

    return 0;
}