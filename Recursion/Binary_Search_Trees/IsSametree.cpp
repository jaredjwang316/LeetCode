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

bool isSameTree(TreeNode* p, TreeNode* q) {
    if (p == nullptr && q == nullptr)
    {
        return true;
    }
    else if (p == nullptr || q == nullptr)
    {
        return false;
    }
    else if  ((p->left == nullptr && q->left != nullptr) || (p->left != nullptr && q->left == nullptr)  )
    {
        return false;
    }
    else if ( (p->right == nullptr && q->right != nullptr) || (p->right != nullptr && q->right == nullptr) )
    {
        return false;
    }        

    if (p->val != q->val )
    {
        return false;
    }
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}

int main()
{
    TreeNode* pleft1 = new TreeNode(2);
    TreeNode* pright1 = new TreeNode(3);
    TreeNode* p1 = new TreeNode(1, pleft1, pright1);

    TreeNode* qleft1 = new TreeNode(2);
    TreeNode* qright1 = new TreeNode(3);   
    TreeNode* q1 = new TreeNode(1, qleft1, qright1);

    cout << "Is p1 and q1 the same tree? " << isSameTree(p1, q1) << endl;
    
    TreeNode* pleft2 = new TreeNode(2);
    TreeNode* p2 = new TreeNode(1, pleft2, nullptr);

    TreeNode* qright2 = new TreeNode(2);   
    TreeNode* q2 = new TreeNode(1, nullptr, qright2);

    cout << "Is p2 and q2 the same tree? " << isSameTree(p2, q2) << endl;

    TreeNode* pleft3 = new TreeNode(2);
    TreeNode* pright3 = new TreeNode(1);
    TreeNode* p3 = new TreeNode(1, pleft3, pright3);

    TreeNode* qleft3 = new TreeNode(1);
    TreeNode* qright3 = new TreeNode(2);   
    TreeNode* q3 = new TreeNode(1, qleft3, qright3);

    cout << "Is p3 and q3 the same tree? " << isSameTree(p3, q3) << endl;
    return 0;

}