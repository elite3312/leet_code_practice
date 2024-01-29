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

/**copy to here**/
int main()
{
	// int cur= min({1,2,3});
	// cout<<cur;

	// unordered_map<int,int>m;
	// m.insert(pair(1,2));
	// cout<<m.find(1)->second;

	vector<int>a={1,2,3};
	int count=0;
	for (auto &e:a){
		if (count==0){
			a.push_back(4);
		}
		count+=1;
		cout<<e<<endl;
	}
	return 0;
}

/*idea
*/