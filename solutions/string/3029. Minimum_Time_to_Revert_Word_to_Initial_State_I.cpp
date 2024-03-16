
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
class Solution {
public:
	bool starts_with(string word,int remaining_right_chars_ptr){
		int res=true,n=word.size();
		int substr_size=n-remaining_right_chars_ptr;
		int j=remaining_right_chars_ptr;
		for(int i=0;i<substr_size;i++){
			if(word[i]!=word[j++])return false;
		}
		return res;
	}
    int minimumTimeToInitialState(string word, int k) {
		int res=0,n=word.size();
		
		int remaining_right_chars_ptr=0;
		do{
			res++;
			if ((n-1-remaining_right_chars_ptr)>=k)
				remaining_right_chars_ptr+=k;
			else break;
			
		}
		while (starts_with(word,remaining_right_chars_ptr)==false);
		
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

