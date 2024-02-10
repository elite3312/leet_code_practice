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
       return a.first<b.first;
}
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int> >& intervals) {
        vector<pair<int,int>>v;
		for (auto e:intervals)
			v.push_back({e[0],e[1]});
		sort(v.begin(),v.end(),myComparison);
		int n=v.size(),to_remove=0;
		int res=0;
		map<pair<int,int>,int>m;
		for (int i=0;i<n-1;i++){
			
			for (int j=i+1;j<n;j++)
				if (v[i].second>v[j].first){
					m[v[i]]++;
					m[v[j]]++;
					to_remove+=1;
				}
			
		}

		vector <int>v1;
		for (auto e:m)v1.push_back(e.second);
		sort(v1.begin(),v1.end());
		for (int i=v1.size()-1;i>=0;i--){
			to_remove-=v1[i];
			if(to_remove<0)break;
			res+=1;
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

