//#include "utils/linked_list.hpp"
//#include "utils/binary_tree.hpp"
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

/**copy from here**/

const int  base=23,mod=1e7+7;
class Solution {
public:
    string shortestPalindrome(string s) {
		/*first find longest Palindrome in s*/
		int n = s.length();
		vector<int> power(n, 1);
		
		// Precompute the powers of the base modulo the mod
		for (int i = 1; i < n; i++) {
			power[i] = (power[i - 1] * base) % mod;
		}
		
		//compute forward_hash and backward_hash for entire string
		int forward_hash=0,backward_hash=0;
        for (int i =0; i < n; i++) {
			forward_hash*=power[i];
			backward_hash*=power[i];

			forward_hash+=int(s[i]);
			backward_hash+=int(s[n-1-i]);

			forward_hash%=mod;
			backward_hash%=mod;

			cout << forward_hash << ' ';
			cout << backward_hash << ' ';
		}

		//find largest i such that s[0:i+1] and s[n-1-i:n+1] have the same forward and backward hash
		int i=n-1;
		while (i){
			if (forward_hash==backward_hash)break;

			forward_hash-=int(s[i]);
			forward_hash/=power[i];
			backward_hash-=int(s[i]);
			backward_hash/=power[n-1-i];

			forward_hash%=mod;
			backward_hash%=mod;
		}

		
		return s.substr(0,i+1);
    }
};
/**copy to here**/
int main()
{
	Solution *sol = new Solution();
	string s;

	s ="abaca";
	cout<<sol->shortestPalindrome(s);

	s ="ababa";
	cout<<sol->shortestPalindrome(s);
    return 0;
}

/*
idea:1.find the longest palinedrome substring in s that starts at 0
	 2.find to_add=s[len("longest palinedrome substring"):]
	 3.res=to_add[::-1]+"longest palinedrome substring"
*/