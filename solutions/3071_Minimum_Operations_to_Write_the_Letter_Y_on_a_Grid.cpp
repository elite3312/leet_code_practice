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
class Solution
{
public:
	int minimumOperationsToWriteY(vector<vector<int>> &grid)
	{
		int cells_on_y[3] = {0, 0, 0}, cells_not_on_y[3] = {0, 0, 0};
		int N = grid.size();
		int center = N / 2;

		for (int r = 0; r < N; r++)
			for (int c = 0; c < N; c++)
				/*upper left*/
				if ((r == c && r < center) ||
					/*upper right*/
					(r == (N - 1 - c) && r < center) ||
					/*bottom*/
					(c == center && r >= center)
					)
					cells_on_y[grid[r][c]] += 1;
				else
					cells_not_on_y[grid[r][c]] += 1;
			/*
			find maximum occurring value, add the remaining 2 values in that partition to res
			
			in the remaining partition, find the maximum occurring value that is different
 			than the previous maximum value. add the remaining 2 values in that partition to res
			*/
			int res=1e5;
			/*01*/
			res=min(res,cells_on_y[1]+cells_on_y[2]+cells_not_on_y[0]+cells_not_on_y[2]);
			/*02*/
			res=min(res,cells_on_y[1]+cells_on_y[2]+cells_not_on_y[0]+cells_not_on_y[1]);
			/*10*/
			res=min(res,cells_on_y[0]+cells_on_y[2]+cells_not_on_y[1]+cells_not_on_y[2]);
			/*12*/
			res=min(res,cells_on_y[0]+cells_on_y[2]+cells_not_on_y[0]+cells_not_on_y[1]);
			/*20*/
			res=min(res,cells_on_y[0]+cells_on_y[1]+cells_not_on_y[1]+cells_not_on_y[2]);
			/*21*/
			res=min(res,cells_on_y[0]+cells_on_y[1]+cells_not_on_y[0]+cells_not_on_y[2]);
			return res;
	}
};

/**copy to here**/
int main()
{
	Solution *sol = new Solution();
	vector<vector<int>>grid={{1,2,2},{1,1,0},{0,1,0}};
	cout<<sol->minimumOperationsToWriteY(grid);//3

	grid={{0,1,0,1,0},{2,1,0,1,2},{2,2,2,0,1},{2,2,2,2,2},{2,1,2,2,2}};
	cout<<sol->minimumOperationsToWriteY(grid);//12
	return 0;
}

/*idea
1. partion cells into on y and not on y
2. for each partition, record sum of each values(0,1,2)
3. res=0
4. find maximum occurring value, add the remaining 2 values in that partition to res
5. in the remaining partition, find the maximum occurring value that is different
 than the previous maximum value. add the remaining 2 values in that partition to res

for example:
	value  		0 1 2
				------
	on_y 		2 2 3
	not_on_y 	3 4 11

	maximum value is 11 in not_on_y, add 3 and 4 to res
	remaining maximum value in on_y that is not the previous maximum value is 1, add 2 and 3 to res
	res=12
*/
