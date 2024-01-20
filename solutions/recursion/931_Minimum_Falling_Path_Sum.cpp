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
    unordered_map<int,int>m;
	int row,col;
	vector<vector<int>> grid;
	int get_key(int r,int c){ return r*col+c;}
    int minFallingPathSum(vector<vector<int>>& matrix) {
		this->grid=matrix;
		row=grid.size();
		col=grid[0].size();
		int res=1e7;

		
		for (int c=0;c<col;c++){
			res=min(res,dfs(0,c));
		}
		return res;
    }
	int dfs(int r,int c){
		if (c<0||r>row-1||c>col-1)return 1e7;
		if(r==row-1)return grid[r][c];

		auto i=m.find(get_key(r,c));
		if (i!=m.end()){
			return (*i).second;
		}
		int cur= min({
			dfs(r+1,c-1),
			dfs(r+1,c),
			dfs(r+1,c+1)
			});
		m.insert(pair(get_key(r,c),cur+grid[r][c]));
		return cur+grid[r][c];
	}
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<vector<int>>matrix = {{2,1,3},{6,5,4},{7,8,9}};
	cout<<s->minFallingPathSum(matrix);
	//13
	matrix.clear();
	matrix = {{2,1,3}};
	cout<<s->minFallingPathSum(matrix);
	//1
	return 0;
}

/*idea
dfs+hash table

use a bottom up approach

2 1 3  14 13 15
6 5 4->13 12 12
7 8 9   7  8  9
*/