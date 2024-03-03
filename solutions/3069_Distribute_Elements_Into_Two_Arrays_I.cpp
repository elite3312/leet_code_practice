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
    vector<int> resultArray(vector<int>& nums) {
        vector<int>a={nums[0]},b={nums[1]};
		for(int i =2;i<nums.size();i++)
			if(a.back()>b.back())a.push_back(nums[i]);
			else b.push_back(nums[i]);
		vector<int>res;
		for(auto i:a)res.push_back(i);
		for(auto i:b)res.push_back(i);
		return res;
    }
};

/**copy to here**/
int main()
{
	Solution *sol = new Solution();
	vector<int>nums = {2,1,3},res;
	res=sol->resultArray(nums);
	for (auto i:res)cout<<i;//231

	nums = {5,4,3,8};
	res=sol->resultArray(nums);
	for (auto i:res)cout<<i;//5348
	
 
    return 0;
}
