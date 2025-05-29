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

//Post Order Traversal touches the left nodes, right nodes, then root
vector<int> postorderTraversal(TreeNode* root) {
    if (root == nullptr)
        return vector<int>();   //return empty vector
    
    vector<int> result = postorderTraversal(root->left);
    vector<int> rightSide = postorderTraversal(root->right);

    result.insert(result.end(), rightSide.begin(), rightSide.end());
    result.push_back(root->val);
    
    return result;  
}

void printVector(vector<int> a)
{
    cout << "[";
    for (auto p = a.begin(); p != a.end(); p++)
    {
        cout << *p << " ";
    }
    cout << "]";
}

int main()
{
    TreeNode* a1 = new TreeNode(3);
    TreeNode* a2 = new TreeNode(2, a1, nullptr);
    TreeNode* a3 = new TreeNode(1, nullptr, a2);
    cout << "PostOrder Traversal of this tree nodes has value "; 
    printVector(postorderTraversal(a3)); 
    cout << " in this order" << endl;

    TreeNode* n6 = new TreeNode(6);
    TreeNode* n7 = new TreeNode(7);
    TreeNode* n9 = new TreeNode(9);
    TreeNode* n4 = new TreeNode(4);
    TreeNode* n5 = new TreeNode(5, n6, n7);
    TreeNode* n8 = new TreeNode(8, n9, nullptr);
    TreeNode* n2 = new TreeNode(2, n4, n5);
    TreeNode* n3 = new TreeNode(3, nullptr, n8);
    TreeNode* root = new TreeNode(1, n2, n3);

    cout << "PostOrder Traversal of this tree nodes has value ";
    printVector(postorderTraversal(root));
    cout << " in this order" << endl;

    //Case for empty tree
    cout << "PostOrder Traversal of this tree nodes has value ";
    printVector(postorderTraversal(nullptr));
    cout << " in this order" << endl; 
    
    //Case for tree with only the root
    TreeNode* c1 = new TreeNode(1);
    cout << "PostOrder Traversal of this tree nodes has value ";
    printVector(postorderTraversal(c1));
    cout << " in this order" << endl;    
    return 0;
}