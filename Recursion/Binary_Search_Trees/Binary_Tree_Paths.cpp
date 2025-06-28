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

void helper(TreeNode* root, string s, vector<string>& allPaths)    {
    if (root == nullptr)
    {
        return;
    }
    else if (root->left == nullptr && root->right == nullptr)   //leaf node with no children
    {
        s = s + to_string(root->val);
        allPaths.push_back(s);
        s = "";
    }
    helper(root->left, s + to_string(root->val) + "->", allPaths);
    helper(root->right, s + to_string(root->val) + "->", allPaths);
}

vector<string> binaryTreePaths(TreeNode* root) {
    vector<string> allPaths;
    helper(root, "", allPaths);
    return allPaths;
}

int main()
{
    TreeNode* a1 = new TreeNode(5);
    TreeNode* a2 = new TreeNode(2, nullptr, a1);
    TreeNode* a3 = new TreeNode(3);
    TreeNode* a4 = new TreeNode(1, a2, a3);
    vector<string> a_result = binaryTreePaths(a4);
    cout << "[";
    for(int i = 0; i < a_result.size() - 1; i++)
    {
        cout << a_result.at(i) << ", ";
    }
    cout << a_result.at(a_result.size() - 1) << "]" << endl;

    TreeNode* b1 = new TreeNode(1);
    vector<string> b_result = binaryTreePaths(b1);
    cout << "[";
    for(int i = 0; i < b_result.size(); i++)
    {
        cout << b_result.at(i) << "]" << endl;
    }

    return 1;
}