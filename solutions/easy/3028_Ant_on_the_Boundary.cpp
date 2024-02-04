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
using namespace binary_tree;
using namespace std;
/**copy from here**/
class Solution {
public:
    int returnToBoundaryCount(vector<int>& nums) {
        int res=0,first=0;
		int cur=0;
		for (auto num : nums){
			cur+=num;
			if (first){
				first=0;
				continue;
			}
			if (cur==0)res++;
		}
		return res;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<int> nums;

	nums={3,2,-3,-4};
	cout<<s->returnToBoundaryCount(nums);//0

	nums={2,3,-5};
	cout<<s->returnToBoundaryCount(nums);//1

	

	
	return 0;
}

