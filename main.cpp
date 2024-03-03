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
    string shortestPalindrome(string s) {

		/*find pal*/
		int  base=23,mod=1e7+7;

		int n = s.length();
		vector<int> power(n + 1, 1);
		// Precompute the powers of the base modulo the mod
		for (int i = 1; i <= n; i++) {
			power[i] = (power[i - 1] * base) % mod;
		}

        /*compute hash for s*/
		int hash=0,
			hash_rev=0;
		for(int i=0;i<n;i++){
			/*compare hash value for window*/
			hash=(hash+power[n-1-i]*s[i])%mod;
			hash_rev=(hash_rev+power[i]*s[i])%mod;
		}

		int longest_paline_right=0;
		for(int i=n-1;i>=0;i--){
			if (hash==hash_rev){longest_paline_right=i;break;}
			hash=(hash-power[n-1-i]*s[i])%mod;
			hash_rev=(hash_rev-power[i]*s[i])%mod;
		}
		return s.substr(0,longest_paline_right+1);
    }
};
/**copy to here**/
int main()
{
	Solution *sol = new Solution();
	string s ="ababa";
	cout<<sol->shortestPalindrome(s);
    return 0;
}

/*
idea:1.find the longest palinedrome substring in s that starts at 0
	 2.find to_add=s[len("longest palinedrome substring"):]
	 3.res=to_add[::-1]+"longest palinedrome substring"
*/