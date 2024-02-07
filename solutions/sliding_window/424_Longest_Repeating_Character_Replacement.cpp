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
    int characterReplacement(string s, int k) {
		int n=s.size();
        unordered_map<char,int>m;
		int res=-1,right,left=0,max_freq=-1;
		for (right=0;right<n;right++){
			m[s[right]]++;

			max_freq=max(max_freq,m[s[right]]);
			// Check if the current window size minus 'maxf' is greater than 'k'
            if ((right - left + 1) - max_freq > k) {
                // If so, move the left pointer and decrease the count of the character at the left
                m[s[left]] -= 1;
                left++;
			}
			else{
				// Update the answer with the maximum window size
                res = max(res, (right - left + 1));
			}
		};

		
		return res;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();

	string a;int k;

	a="ABAB";
	k=2;
	cout<<s->characterReplacement(a,k);
	return 0;
}

