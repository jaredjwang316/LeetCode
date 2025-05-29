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

bool isMirror(TreeNode* theLeft, TreeNode* theRight)   {
    if (theLeft == nullptr && theRight == nullptr)
    {
        return true;
    }
    else if (theLeft == nullptr || theRight == nullptr)
    {
        return false;
    }

    if (theLeft->val != theRight->val)
    {
        return false;
    }

    return isMirror(theLeft->left, theRight->right) && isMirror(theLeft->right, theRight->left);
}

bool isSymmetric(TreeNode* root) {
    return isMirror(root->left, root->right);
}

int main()
{
    TreeNode* a1 = new TreeNode(3);
    TreeNode* a2 = new TreeNode(4);
    TreeNode* a3 = new TreeNode(4);
    TreeNode* a4 = new TreeNode(3);
    TreeNode* a5 = new TreeNode(2, a1, a2);
    TreeNode* a6 = new TreeNode(2, a3, a4);
    TreeNode* a7 = new TreeNode(1, a5, a6);

    cout << "Is this tree Symmetric? " << isSymmetric(a7) << endl; 

    TreeNode* b1 = new TreeNode(3);
    TreeNode* b2 = new TreeNode(3);
    TreeNode* b3 = new TreeNode(2, nullptr, b1);
    TreeNode* b4 = new TreeNode(2, nullptr, b2);
    TreeNode* b5 = new TreeNode(1, b3, b4);
    cout << "Is this tree Symmetric? " << isSymmetric(b5) << endl; 
    return 0;
}