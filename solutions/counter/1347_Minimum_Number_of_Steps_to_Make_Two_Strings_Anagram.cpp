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
	bool cmp(const char *&a,const char *&b){
		return*a<*b;
	}
    int minSteps(string s, string t) {
        unordered_map<char,int>s_char_count,t_char_count;
		for (char c='a';c<='z';c++){
			s_char_count[c]=0;
			t_char_count[c]=0;
		}
		for (int i=0;i<s.size();i++){
			s_char_count[s[i]]++;
			t_char_count[t[i]]++;
		}

		
		int res=0;//,leftover=0;
		for (char c='a';c<='z';c++){
			if( s_char_count[c]==t_char_count[c])continue;
			int diff=abs(s_char_count[c]-t_char_count[c]);
			// if (leftover>=0){
			// 	if (leftover>diff){
			// 		leftover-=diff;diff=0;
			// 	}
			// 	else{diff-=leftover;leftover=0;}
			// }
			// res+=diff;
			// leftover+=diff;
			res+=diff;
		}
		return res/2;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	string a="ftngfmcxlfxitnoanvnnfdswndjhgclcbcyrkcwqwlglqylgrcbr",b="mnpyqiuogwvgjsrzljxryzsqlxatmpkauuemgkxmgshkfdwnpcet";
	cout<<s->minSteps(a,b)<<endl;//20
	
	a="aab",b="bba";
	cout<<s->minSteps(a,b)<<endl;//1
	
	a="leetcode",b="practice";
	cout<<s->minSteps(a,b)<<endl;//5
	
	a="anagram",b="mangaar";
	cout<<s->minSteps(a,b)<<endl;//0
	return 0;
}

/*idea
use 2 hashmaps to store char count from each string
iterate thru chars and sum abs(map_s[char]-map_t[char])
then return sum/2, since for each operation you change 2 char occurences

*/