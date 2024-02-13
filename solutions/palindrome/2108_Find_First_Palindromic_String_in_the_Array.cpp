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

class Solution_0 {
public:
    bool isPalindrome(string&s){
		int j=s.size()-1,i=0;
		while (i<=j){
			if(s[i]!=s[j])return false;
			j--;i++;}
		return true;
	}
    string firstPalindrome(vector<string>& words) {
        for (auto s:words){
			if(isPalindrome(s))return s;
		}
		return string("");
    }
};
class Solution{
public:
    
    string firstPalindrome(vector<string>& words) {
		int i,j;bool is_pal;
        for (auto s:words){
			j=s.size()-1;i=0;is_pal=true;

			while (i<=j){
				if(s[i]!=s[j]){
					is_pal=false;break;
				}
				j--;i++;
			}
			if( is_pal)return s;
			

		}
		return string("");
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector <string> w;
	w={string("aba"),string("cool")};
	cout<<s->firstPalindrome(w);
	
	w={string("lool"),string("cool")};
	cout<<s->firstPalindrome(w);
	return 0;
}

