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
    vector<int> countBits(int n) {
        vector<int> res={0};
		int binary_rep[32]={0},cur;
		int bit_count=0;
		for (int i =1 ;i<n+1;i++){
			cur=31;
			while( binary_rep[cur]==1){
				binary_rep[cur]=0;
				cur-=1;
				bit_count-=1;
			}
			binary_rep[cur]=1;
			bit_count+=1;
			res.push_back(bit_count);
		}
		return res;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	int n=2;
	auto res=s->countBits(n);
	for (auto e :res)
		cout<<e;	//011
	return 0;
}

