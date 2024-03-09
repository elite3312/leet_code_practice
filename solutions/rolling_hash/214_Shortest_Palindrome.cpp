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
/*the idea of rolling hash is:
s=abcd

h(abcd)=h(1,2,3,4)
=1*(base^3)+2*(base^3)+3*(base^2)+4*(base^0)

h(bcde)=h(2,3,4,5)
=h(abcd)-1*base^3)*10+5*(base^0)
...
*/
const int  base=23,mod=1e7+7;
class Solution {
public:
    string shortestPalindrome(string s) {
		/*first find longest Palindrome in s*/
		/*we do so by rolling hash:
		forward_hashs=[s[0]*pow[0],
					   s[0]*pow[0]+s[1]*pow[1],
					   ...,
					   s[n-1]*pow[n-1]+s[n-1]*pow[n-1],
					 =[s[0]*pow[0],
					  forward_hashs[0]+s[1]*pow[1],
					   ...,
					   forward_hashs[n-2]+s[n-1]*pow[n-1],
		
		backward_hashs=[s[0]*pow[0],
					   forward_hashs[0]*base+s[1],
					   ...,
					   forward_hashs[n-2]*base+s[n-1],
		*/
		int n = s.length();
		if(n==0||n==1)return s;
		vector<int> power(n, 1);
		
		// Precompute the powers of the base modulo the mod
		for (int i = 1; i < n; i++) {
			power[i] = (power[i - 1] * base) % mod;
		}
		//power=1,base,base^2...base^(n-1)

		//compute forward_hashs and backward hashes

		vector<long long> forward_hashs(n, 0);
		forward_hashs[0]=s[0]*power[0]%mod;
		vector<long long> backward_hashs(n, 0);
		backward_hashs[0]=forward_hashs[0];

		for(int i = 1; i < n; i++){
			forward_hashs[i]=(forward_hashs[i-1]+s[i]*power[i])%mod;
			backward_hashs[i]=(backward_hashs[i-1]*base+s[i])%mod;
		}
		int longest_paline_right=-1;
		for (int i = n-1; i >-1; i--)if(forward_hashs[i]==backward_hashs[i]){longest_paline_right=i;break;}
		string temp= s.substr(longest_paline_right+1);
		reverse(temp.begin(),temp.end());
		return temp+s;
    }
};
/**copy to here**/
int main()
{
	Solution *sol = new Solution();
	string s;

	s ="abaca";
	cout<<sol->shortestPalindrome(s)<<endl;

	s ="ababa";
	cout<<sol->shortestPalindrome(s)<<endl;
	s ="";
	cout<<sol->shortestPalindrome(s)<<endl;
	s ="a";
	cout<<sol->shortestPalindrome(s)<<endl;
	s ="aa";
	cout<<sol->shortestPalindrome(s)<<endl;;
    return 0;
}

/*
idea:1.find the longest palinedrome substring in s that starts at 0
	 2.find to_add=s[len("longest palinedrome substring"):]
	 3.res=to_add[::-1]+"longest palinedrome substring"
*/