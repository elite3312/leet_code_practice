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
/**copy from here**/
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int> >& intervals) {
        vector<pair<int,int>>v;
		for (auto e:intervals)v.push_back({e[0],e[1]});
		return 0;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<vector<int> > intervals={{1,2},{2,3},{3,4},{1,3}};
	cout<<s->eraseOverlapIntervals(intervals);
	return 0;
}

