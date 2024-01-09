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
    int minOperations(vector<int>& nums, int k) {
        int cur=nums[0];
		for(int i =1;i<nums.size();i++)cur^=nums[i];
		cur^=k;
		int res=0;
		while (cur){
			if (cur&1)res+=1;
			cur>>=1;
		}
		return res;
    }

};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector <int>nums={2,1,3,4};int k=1;
	cout<<s->minOperations(nums,k);//2
	return 0;
}

/*idea
bitwise xor will leave bits with odd number of 1s as 1, and 
bits with even number of 1s as 0
*/