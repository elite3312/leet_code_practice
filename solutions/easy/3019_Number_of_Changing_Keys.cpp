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
    int countKeyChanges(string s) {
        int last_key=-1,res=0;
		for (auto c :s){
			int cur=c;
			if (last_key!=cur){
				if (abs(last_key-cur)!=32)res++;
			}
			
			last_key=cur;
		}
		return res-1;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	string a;
	int res;

	a="aAbBcC";
	res=s->countKeyChanges(a);
	cout<<res<<endl;//3

	

	
	return 0;
}

