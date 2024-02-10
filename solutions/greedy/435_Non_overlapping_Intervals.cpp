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
bool myComparison(const pair<int,int> &a,const pair<int,int> &b)
{
       return a.second<b.second;
}
class Solution {
public:
	
    int eraseOverlapIntervals(vector<vector<int> >& intervals) {
		int res=0;
        vector<pair<int,int>>v;
		for (auto e:intervals)v.push_back({e[0],e[1]});
		sort(v.begin(),v.end(),myComparison);
		
		int end=v[0].second;
		for (int i=1;i<v.size();i++){
			if (v[i].first<end)res+=1;
			else end=v[1].second;
		}
		return res;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<vector<int> > intervals={{1,2},{2,3},{3,4},{1,3}};
	cout<<s->eraseOverlapIntervals(intervals);//1
	intervals={{1,2},{1,2},{1,2}};
	cout<<s->eraseOverlapIntervals(intervals);//2
	return 0;
}

