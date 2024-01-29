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
    int maximumLength(vector<int>& nums) {
        if (nums.size()==1)return 1;

		unordered_map<int,int>ctr;
		for (auto num: nums)ctr[num]+=1;
	
		int _sum,res=0,center;
		vector<int> keys;
		for (auto e : ctr)keys.push_back(e.first);
		for (auto e : keys){
			if (e==1)continue;

			center=e;
			_sum=1;
			double _sqrt=sqrt(center);
			if (_sqrt-floor(_sqrt)>0){
				//not a perfect square
				continue;
			}
			center=int(_sqrt);
			while (ctr[center]>=2){
				_sum+=2;
				_sqrt=sqrt(center);
				if (_sqrt-floor(_sqrt)>0){
					//not a perfect square
					break;
				}
				center=int(_sqrt);
			}
			
			res=max(res,_sum);

		}
		
		int _one_len=ctr[1];
		if( _one_len%2==0)_one_len-=1;
		return max(res,_one_len);

    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<int>a;
	int res;

	a={64,25,121,81,49,100,49,36,81,64,25,81,36,36,4,49,81,9,49,100,49,36,100,36,4,49,25,100,25,25,64,4,100,25,16,16,64,144,4,16,25,144,121,9,49,4,100,144,64,36,100,81,4,16,64,64,4,64,25,121,49,49,16,144,36,144,144,25,64,25,100,100,4,16,81,49,4,121,16,100,100,144,9,144,25,9,64,16,36,36,25,64,36,121,64,49,25,81,121,64};
	res=s->maximumLength(a);
	cout<<res<<endl;//3

	a={48841,358801,28561,18974736,4356,221,358801,599,13,4356,66,48841,28561,815730721,13,815730721,18974736,66,169,599,169,221};
	res=s->maximumLength(a);
	cout<<res<<endl;//7
	a={5,4,1,2,2};
	res=s->maximumLength(a);
	cout<<res<<endl;//3

	
	return 0;
}

