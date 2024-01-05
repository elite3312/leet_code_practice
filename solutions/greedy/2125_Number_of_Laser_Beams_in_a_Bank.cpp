#include "utils/linked_list.hpp"
#include "utils/binary_tree.hpp"
/**copy from here**/
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstring>
using namespace binary_tree;
using namespace std;
class Solution {
public:
    int numberOfBeams_0(vector<string>& bank) {
		if (bank.size()==1)return 0;
        vector<int> lasers;
		for (auto row:bank){
			int one_count=0;
			for (auto c:row)if(c=='1')one_count++;
			if (one_count>0)lasers.push_back(one_count);
		}
		//lasers={3,0,2,1}
		if (lasers.size()<=1)return 0;
		int res=0;
		for (int i=0;i<lasers.size()-1;i++)res+=lasers[i]*lasers[i+1];
		//3x2+2x1=8
		return res;
    }
	int numberOfBeams(vector<string>& bank) {
		if (bank.size()==1)return 0;
		int res=0,last,cur,non_zero_rows_count=0;
		bool is_first=true;
		for (auto row:bank){
			int one_count=0;
			for (auto c:row)if(c=='1')one_count++;
			if (one_count>0){
				non_zero_rows_count++;
				cur=one_count;
				if (non_zero_rows_count>=2)
					res+=last*cur;
				last=cur;
			}
		}
		return res;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<string> bank = {"011001","000000","010100","001000"};
	cout<<s->numberOfBeams(bank);

	bank.clear();
	bank= {"000","111","000"};
	cout<<s->numberOfBeams(bank);
	return 0;
}

/*idea
011001
000000
010100
001000

3x2+2x1=8
*/