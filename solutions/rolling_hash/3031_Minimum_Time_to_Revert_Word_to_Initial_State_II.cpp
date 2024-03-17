#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstring>
#include <math.h>
#include <map>

/*this will cause tle*/
using namespace std;
const int  base=23,base1=31,mod=1e7+7;
class Solution {
public:
	
    int minimumTimeToInitialState(string word, int k) {
		int res=0,n=word.size();
		

		/*compute forward_hashs for word*/
		long long forward_hash=0,forward_hash1=0,pow=1,pow1=1;
		map<pair<int,int>,bool>h;
		
		for(int i = 0; i < n; i++){
			forward_hash=(forward_hash+word[i]*pow)%mod;
			pow=pow*base%mod;
			forward_hash1=(forward_hash1+word[i]*pow1)%mod;
			pow1=pow1*base1%mod;
			h[{forward_hash,forward_hash1}]=true;
		}

		// creating isprefix array that tells if the substring word.substr(i) is also a prefix of word or not
		vector<bool>isprefix(n,false);
		long long backward_hash=0,backward_hash1=0;
        for(int i = n-1;i>=0;i--){
            backward_hash1 = (backward_hash1*base1+word[i])%mod;
            backward_hash = (backward_hash*base+word[i])%mod;
            if(h.find({backward_hash,backward_hash1})!=h.end())isprefix[i]=true;
			
        }

		int remaining_right_chars_ptr=0;
		do{
			res++;
			if ((n-1-remaining_right_chars_ptr)>=k)
				remaining_right_chars_ptr+=k;
			else break;
			
		}
		while (isprefix[remaining_right_chars_ptr]==false);
		
		
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

