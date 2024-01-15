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
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int,int>m;
		int cur_max_freq=-1;
		for (auto num:nums){
			m[num]+=1;
			if (m[num]>cur_max_freq)cur_max_freq=m[num];
		}
		int res=0;
		for (auto freq:m)
			if (freq.second==cur_max_freq)res+=cur_max_freq;
		return res;

    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	
	return 0;
}

/*idea
use counter to record occurences

*/