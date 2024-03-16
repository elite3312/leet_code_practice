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
	
    int minimumTimeToInitialState(string word, int k) {
		int res=0,n=word.size();

		/*Precompute the powers of the base modulo the mod*/
		vector<int> power(n, 1);
		for (int i = 1; i < n; i++) {
			power[i] = (power[i - 1] * base) % mod;
		}

		/*compute forward_hashs for word*/
		vector<long long> forward_hashs(n, 0);
		forward_hashs[0]=word[0]*power[0]%mod;
		for(int i = 1; i < n; i++)
			forward_hashs[i]=(forward_hashs[i-1]+word[i]*power[i])%mod;
		
		/*same logic from 3029*/
		int right_len=n,right_hash=forward_hashs[n-1];
		while(1){
			res++;
			if (right_len-1>=k){
				right_len-=k;
				for(int i=0;i<k;i++)
					right_hash=(right_hash-word[n-right_len+i]*power[n-right_len+i])/base%mod;
			}
			else break;
			
			if (forward_hashs[right_len-1]==right_hash)break;
		}
		
		return res;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	//string a="123412";
	//auto t1=s->starts_with(a,1);
	//auto t2=s->starts_with(a,4);
	//return 0;
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

