#include "utils/linked_list.hpp"
#include "utils/binary_tree.hpp"
/**copy from here**/
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace binary_tree;
using namespace std;

class Solution
{
public:
    TreeNode *lowestCommonAncestor(TreeNode *cur, TreeNode *p, TreeNode *q)
    {
        if (!cur)return NULL;
        else if( cur == p || cur == q)
            return cur;

        TreeNode *left = lowestCommonAncestor(cur->left, p, q);
        TreeNode *right = lowestCommonAncestor(cur->right, p, q);
        
        if (left &&right)return cur;
        else if (!left && right)return right;
        else if (left && !right)return left;
        else return NULL;
    }
} ;

/**copy to here**/
int main()
{
    Solution *s = new Solution();
    TreeNode*root=new TreeNode(3);
    root->left=new TreeNode(5);
    root->right=new TreeNode(1);

    root->left->left=new TreeNode(6);
    root->left->right=new TreeNode(2);

    
    root->left->right->left=new TreeNode(7);
    root->left->right->right=new TreeNode(4);

    root->right->left=new TreeNode(0);
    root->right->right=new TreeNode(8);
    cout<<s->lowestCommonAncestor(root,root->left->right->right,root->left->left)->val;
    //5
    return 0;
}
/*idea:
If the current (sub)tree contains both p and q, then the function result is their LCA.
If only one of them is in that subtree, then the result is that one of them.
If neither are in that subtree, the result is null/None/nil.
*/
