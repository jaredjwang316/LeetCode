#include <iostream>
using namespace std;

/**
 * Problem Description:
 * Given the root of a binary tree and an integer targetSum, return true if the tree has a 
 * root-to-leaf path such that adding up all the values along the path equals targetSum.
 * Otherwise, return false;
 * A leaf is a node with no children.
 */

//Definition for a binary tree node.
struct TreeNode {
    int val;     
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

bool hasPathSum(TreeNode* root, int targetSum)  {
    if (root == nullptr)    //no root-to-leaf paths
    {
        return false;
    }
    else if (root->left == nullptr && root->right == nullptr && targetSum == root->val)
    {
        return true;
    }
    return hasPathSum(root->left, targetSum - root->val) || hasPathSum(root->right, targetSum - root->val);
}

int main()
{
    TreeNode* a1 = new TreeNode(7);
    TreeNode* a2 = new TreeNode(2);
    TreeNode* a3 = new TreeNode(11, a1, a2);
    TreeNode* a4 = new TreeNode(4, a3, nullptr);
    TreeNode* a5 = new TreeNode(1); 
    TreeNode* a6 = new TreeNode(4, nullptr, a5);
    TreeNode* a7 = new TreeNode(13);
    TreeNode* a8 = new TreeNode(8, a7, a6);
    TreeNode* a9 = new TreeNode(5, a4, a8);

    cout << "Is there a root-to-leaf path in tree a9 with targetSum = 22? " << hasPathSum(a9, 22) << endl;;
    cout << "Is there a root-to-leaf path in tree a9 with targetSum = 17? " << hasPathSum(a9, 17) << endl;
    cout << "Is there a root-to-leaf path in tree a9 with targetSum = 18? " << hasPathSum(a9, 18) << endl;

    TreeNode* b1 = new TreeNode(2);
    TreeNode* b2 = new TreeNode(3);
    TreeNode* b3 = new TreeNode(1, b1, b2);
    cout << "Is there a root-to-leaf path in tree b3 with targetSum = 5? " << hasPathSum(b3, 5) << endl;

    cout << "Is there a root-to-leaf path in an empty tree with targetSum = 0? " << hasPathSum(nullptr, 0) << endl;    
    return 0;
}