#include "utils/linked_list.hpp"
#include "utils/binary_tree.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstring>
using namespace binary_tree;
using namespace std;
/**copy from here**/
class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int longest_sequential_prefix_sum=nums[0];
		int pre=nums[0];
		unordered_map<int,bool> m;
		m[nums[0]]=true;
		int sequential_prefix_is_done=false;
		for (int i =1 ;i<nums.size();i++){
			m[nums[i]]=true;
			if (!sequential_prefix_is_done&&nums[i]==pre+1){
				longest_sequential_prefix_sum+=nums[i];
			}
			else
				sequential_prefix_is_done=true;
			
			pre=nums[i];
			
		}
		int res=longest_sequential_prefix_sum;
		while (true)
			if (m[res]==true)res+=1;//(8+4)*5/2
			else 
				return res;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<int> v={4,5,6,7,8,8,9,4,3,2,7};
	cout<<s->missingInteger(v);
	vector<int> v1={3,4,5,1,12,14,13,15};//16
	cout<<s->missingInteger(v1);
	vector<int> v2={1,2,3,2,5};
	cout<<s->missingInteger(v2);//6

	return 0;
}

/*idea
use map to record all elements
find the seq prefix sum
find 1st number bigger than seq prefix sum and not in map
*/