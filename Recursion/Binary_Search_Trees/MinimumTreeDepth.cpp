#include <iostream>
using namespace std;

/**
 * Problem Description: Given a binary tree, find its minimum depth.  The minimum depth is the number 
 * of nodes along the shortest path from the root node down to the nearest leaf node.
 * Note: A leaf is a node with no children.
 * 
 * Constraints: The number of nodes in the tree is in the range [0, 10^5].
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

int minDepth(TreeNode* root) {
    if (root == nullptr)
    {
        return 0;
    }
    else if (root->left == nullptr)
    {
        return 1 + minDepth(root->right);
    }
    else if (root->right == nullptr)
    {
        return 1 + minDepth(root->left);  
    }
    return 1 + min(minDepth(root->left), minDepth(root->right));
}


int main()
{
    TreeNode* a1 = new TreeNode(15);
    TreeNode* a2 = new TreeNode(7);
    TreeNode* a3 = new TreeNode(20, a1, a2);
    TreeNode* a4 = new TreeNode(9);
    TreeNode* a5 = new TreeNode(3, a4, a3);
    cout << minDepth(a5) << endl;   //2

    TreeNode* b1 = new TreeNode(6);
    TreeNode* b2 = new TreeNode(5, nullptr, b1);
    TreeNode* b3 = new TreeNode(4, nullptr, b2);
    TreeNode* b4 = new TreeNode(3, nullptr, b3);
    TreeNode* b5 = new TreeNode(2, nullptr, b4);
    cout << minDepth(b5) << endl;   //5

    TreeNode* c1 = new TreeNode(4);
    TreeNode* c2 = new TreeNode(5);
    TreeNode* c3 = new TreeNode(3, c1, c2);
    TreeNode* c4 = new TreeNode(2);
    TreeNode* c5 = new TreeNode(1, c4, c3);
    cout << minDepth(c5) << endl;   //2
    
    return 0;
}