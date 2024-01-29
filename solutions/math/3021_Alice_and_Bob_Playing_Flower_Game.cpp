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
    long long flowerGame(int n, int m) {
        /*1 find "number of even number <=n" and "number of even odd <=n" */
		long long n_odd,n_even,m_odd,m_even;
		if (n%2==1){
			n_odd=(n+1)/2;
			n_even=(n-1)/2;
		}else {
			n_odd=(n)/2;
			n_even=(n)/2;
		}
		/*2 do the same for m*/
		if (m%2==1){
			m_odd=(m+1)/2;
			m_even=(m-1)/2;
		}else {
			m_odd=(m)/2;
			m_even=(m)/2;
		}
		return n_even*m_odd+m_even*n_odd;



    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	int n=2,m=3;
	auto res=s->flowerGame(n,m);
	cout<<res<<endl;//3

	n=100000;m=10000;
	res=s->flowerGame(n,m);
	cout<<res;//3
	return 0;
}

