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
    int minimumTimeToInitialState(string word, int k) {
		int res=0;
		
		string remaining_right_chars=word;
		do{
			res++;
			if (remaining_right_chars.size()>=k)
				remaining_right_chars=remaining_right_chars.substr(k);
			else break;
			
		}
		while (word.find(remaining_right_chars)!=0);
		
		return res;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<int> nums;

	string w;int k;

	w="aab";k=2;
	cout<<s->minimumTimeToInitialState(w,k);//2

	w="aa";k=1;
	cout<<s->minimumTimeToInitialState(w,k);//1

	w="abacaba";k=3;
	cout<<s->minimumTimeToInitialState(w,k);//2

	w="abacaba";k=4;
	cout<<s->minimumTimeToInitialState(w,k);//1

	w="abcbabcd";k=2;
	cout<<s->minimumTimeToInitialState(w,k);//4
	
	return 0;
}

