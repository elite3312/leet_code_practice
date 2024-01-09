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
using namespace binary_tree;
using namespace std;
/**copy from here**/

class Solution {
public:
    int res=0,low,high;
    int rangeSumBST(TreeNode* root, int low, int high) {
		this->low=low;
		this->high=high;
		inorder(root);
		return res;
    }
	void inorder(TreeNode* cur){
		if (cur==NULL)return;
		inorder(cur->left);
		if(cur->val<=high && cur->val>=low)res+=cur->val;
		inorder(cur->right);
	}
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	
	return 0;
}

/*idea
*/