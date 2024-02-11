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
using namespace binary_tree;
/**copy from here**/
class Solution {
public:
    int countSubstrings(string s) {
        int res=0,n=s.size();
		for (int i=0;i<n;i++){
			//find longest ood palindrome centered at i
			int l=0;
			while(1){
				if ((i-l)<0||(i+l)>(n-1))break;
				if(s[i-l]==s[i+l])res++;
				else break;
				l++;
			}
			//find longest even palindrome centered at i
			l=0;
			
			while(1){
				if((i-l)<0||(i+1+l)>(n-1))break;
				if(s[i-l]==s[i+1+l])res++;
				else break;
				l++;
			}

		}
		return res;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	string a;
	a="abc";
	cout<<s->countSubstrings(a);//3
	a="aaa";
	cout<<s->countSubstrings(a);//6
	return 0;
}

/*idea
expand from middle
*/