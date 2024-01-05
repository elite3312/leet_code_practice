#include "utils/linked_list.hpp"
#include "utils/binary_tree.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstring>
using namespace binary_tree;
using namespace std;
/**copy from here**/
class Solution
{
public:
	int minOperations(vector<int> &nums)
	{
		// hasmmap to count occurences
		unordered_map<int, int> num_count;
		for (auto num : nums)
			num_count[num]++;

		int res = 0;
		for (auto pair : num_count)
		{
			int count = pair.second;
			if (count == 1)
				return -1;
			else if (count == 2 || count == 3)
				res += 1;
			else
			{ // greater or equal to 4
				if (count % 3 == 0)
					res += count / 3;
				else
				{
					int three_count = count / 3;
					for (int i = three_count; i >= 0; i--)
					{
						int threes_removed = count - 3 * i;
						if (threes_removed % 2 == 0)
						{
							res += i + threes_removed / 2;
							break;
						}
					}
				}
			}
		}
		return res;
	}
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<int> nums = {2, 3, 3, 2, 2, 4, 2, 3, 4};
	cout << s->minOperations(nums); // 4

	nums.clear();
	nums = {2, 1, 2, 2, 3, 3};
	cout << s->minOperations(nums); //-1
	return 0;
}

/*idea
any number greater than 2 can be composed of 2s and 3s
for numbers greater than 4, try to maximize the number 3s in the composition with a greedy approach.
*/