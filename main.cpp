#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstring>
#include <math.h>
#include <map>
#include <bitset>
using namespace std;
/**copy from here**/
class Solution
{
public:
	int numMagicSquaresInside(vector<vector<int>> &grid){
		// edge case
		int m = grid.size(), n = grid[0].size();
		if (m < 3 || n < 3)
			return 0;

		int res = 0;
		/*for each upper left i,j*/
		for (int i = 0; i < m - 3 + 1; i++)
			for (int j = 0; j < n - 3 + 1; j++)
			{
				/*check if numbers are distinct*/
				bitset<10> once;
				bool isDisdinct=true;
				for (int n_i=0;n_i<3;n_i++){
					for (int n_j=0;n_j<3;n_j++)
						if (grid[i+n_i][j+n_j]>9||grid[i+n_i][j+n_j]==0||//only allow 1 to 15
							once[grid[i+n_i][j+n_j]])//if it already appeared, then it is not distinct
							{
								isDisdinct=false;
								break;
							}
						else
							once.flip(grid[i+n_i][j+n_j]);
					if (!isDisdinct)
						break;
				}
				if (!isDisdinct)
					continue;
				
				//check equal sums
				/*rows*/
				int sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]; // row 0
				if (sum != grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2]) // row 1
					continue;
				if (sum != grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]) // row 2
					continue;

				/*cols*/
				if (sum != grid[i][j] + grid[i + 1][j] + grid[i + 2][j]) // col 0
					continue;
				if (sum != grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]) // col 1
					continue;
				if (sum != grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]) // col 2
					continue;

				/*diagonals*/
				if (sum != grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]) // col 2
					continue;
				if (sum != grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]) // col 2
					continue;

				res += 1;
			}

		return res;
	}
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<vector<int>> a = {{4, 3, 8, 4},
							 {9, 5, 1, 9},
							 {2, 7, 6, 2}};
	cout << s->numMagicSquaresInside(a);

	vector<vector<int>> b = {{5, 5, 5, 5},
							 {5, 5, 5, 5},
							 {5, 5, 5, 5}};
	cout << s->numMagicSquaresInside(b);

	return 0;
}
