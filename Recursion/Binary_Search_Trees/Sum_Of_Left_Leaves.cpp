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

/* 
Problem Desciption: 
    Given the root of a binary tree, return the sum of all left leaves.
    A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
*/
int sumOfLeftLeaves(TreeNode* root) {
    if (root == nullptr)
    {
        return 0;
    }
    else if (root->left != nullptr && root->left->left == nullptr && root->left->right == nullptr)
    {
        return root->left->val + sumOfLeftLeaves(root->right);
    }
    return sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
}

int main()
{
    TreeNode* a1 = new TreeNode(15);
    TreeNode* a2 = new TreeNode(7);
    TreeNode* a3 = new TreeNode(20, a1, a2);
    TreeNode* a4 = new TreeNode(9);
    TreeNode* a5 = new TreeNode(3, a4, a3);
    cout << sumOfLeftLeaves(a5) << endl;

    TreeNode* b1 = new TreeNode(1);
    cout << sumOfLeftLeaves(b1) << endl;
    return 0;
}