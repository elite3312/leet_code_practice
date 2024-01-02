#include "utils/linked_list.hpp"
#include "utils/binary_tree.hpp"
/**copy from here**/
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstring>
using namespace binary_tree;
using namespace std;
class Solution
{
public:
	vector<vector<int>> findMatrix(vector<int> &nums)
	{
		unordered_map<int, int> occurences;
		for (auto i : nums)
		{
			if (occurences.find(i) == occurences.end())
			{
				occurences[i] = 1;
			}
			else
				occurences[i]++;
		}
		vector<tuple<int, int>> v;
		for (auto i : occurences)
		{
			v.push_back(i);
		}
		sort(v.begin(), v.end(), [](auto const &t1, auto const &t2)
			 { return get<1>(t1) > get<1>(t2); } // lambda
		);
		vector<vector<int>> res;
		for (int i = 0; i < get<1>(v[0]); i++)
		{
			vector<int> new_vec = {get<0>(v[0])};
			res.push_back(new_vec);
		}
		for (int i = 1; i < v.size(); i++)
		{
			int key = get<0>(v[i]);
			int count = get<1>(v[i]);

			for (int j = 0; j < count; j++)

				res[j].push_back(key);
		}
		return res;
	}
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<int> v = {1, 1, 1, 2, 2, 4};
	//{{1,2,4},{1,2},{1,1,1}};
	for (auto i : s->findMatrix(v))
	{
		for (auto j : i)
			cout << j;
		cout << endl;
	}
	vector<int> v1 = {1,3,4,1,2,3,1};
	//{{1,2,3,4},{1,3},{1}};
	for (auto i : s->findMatrix(v1))
	{
		for (auto j : i)
			cout << j;
		cout << endl;
	}
	vector<int> v2 ={9,8,8,4,9,8,8,3,9};
	//
	for (auto i : s->findMatrix(v2))
	{
		for (auto j : i)
			cout << j;
		cout << endl;
	}
	
	return 0;
}

/*idea
arr = [2,1,1,1,2,4]

111
22
4

1:3
2:2
4:1

res=[
	1,2,4
	1,2
	1,
]
*/