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

int maxDepth(TreeNode* root) {
    while(root == nullptr)
        return 0;
    
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}

int main()  {
    TreeNode* a = new TreeNode(15);
    TreeNode* b = new TreeNode(7);
    TreeNode* c = new TreeNode(9);
    TreeNode* d = new TreeNode(20, a, b); 
    TreeNode* e = new TreeNode(3, c, d);   

    cout << "The maximum depth of this tree is " << maxDepth(e) << " nodes" << endl;

    TreeNode* f = new TreeNode(2);
    TreeNode* g = new TreeNode(1, nullptr, f);

    cout << "The maximum depth of this tree is " << maxDepth(g) << " nodes" << endl;
    return 0;
}