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
#include <set>
using namespace std;
using namespace binary_tree;
/**copy from here**/
class Solution {
public:
    int countSubmatrices(vector<vector<int>>& grid, int k) {
        int res=0,R=grid.size(),C=grid[0].size(),
		r,c;
		vector<int>prefix_sums(C,0);
		int cur_row_sum=0;
		for (c=0;c<C;c++)
		{
			cur_row_sum+=grid[0][c];
			prefix_sums[c]=cur_row_sum;
			if (prefix_sums[c]<=k)res++;
		}

		for (r=1;r<R;r++){
			int cur_row_sum=0;
			for (c=0;c<C;c++)
			{
				cur_row_sum+=grid[r][c];
				prefix_sums[c]+=cur_row_sum;
				if (prefix_sums[c]<=k)res++;
			}
		}
		return res;
    }
};

/**copy to here**/
int main()
{
	Solution *sol = new Solution();
	vector<vector<int>> grid;
	int k;

	grid={{7,6,3},{6,6,1}};
	k=18;

	cout<<sol->countSubmatrices(grid,k);//4

	grid={{7,2,9},{1,5,0},{2,6,6}};
	k=20;

	cout<<sol->countSubmatrices(grid,k);//6
 
    return 0;
}

/*
idea:
create an array the size of cols, cols the grid[0].size().
This array serves as the prefix sums of the current row.

res=0
for each row:
	cur_row_sum=0
	for each prefix_sum in array:
		cur_row_sum+=cur_elem
		prefix_sum+=cur_row_sum
		if(prefix_sum<=k)res++

for example:
	input:
	763
	661
	prefix sum:
	7 13 16
	13 19 20
	fillup ordering
	1 2 3
	4 5 6
*/