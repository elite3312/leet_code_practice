#include "utils/linked_list.hpp"
#include "utils/binary_tree.hpp"
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstring>
#include <math.h>
#include <map>
using namespace std;
using namespace binary_tree;
/**copy from here**/

class Solution {
public:
	bool dfs(TreeNode* root,TreeNode* subRoot){
		if (root==NULL &&subRoot==NULL)return true;
		if (root==NULL &&subRoot!=NULL)return false;
		if (root!=NULL &&subRoot==NULL)return false;
		if (root->val!=subRoot->val)return false;

		bool left,right;
		left=dfs(root->left , subRoot->left);
		right=dfs(root->right , subRoot->right);
		return left&&right;
	}
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root)return false;
		
		bool res=false;
		res|=dfs(root,subRoot);
		res|=isSubtree(root->left,subRoot);
		res|=isSubtree(root->right,subRoot);
		return res;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	
	return 0;
}

