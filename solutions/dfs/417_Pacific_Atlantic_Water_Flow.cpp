#include "utils/linked_list.hpp"
#include "utils/binary_tree.hpp"
#include "utils/vector_utils.hpp"
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
class Solution
{
public:
	
	int m, n;
	vector<vector<int>> pacificAtlantic(vector<vector<int>> &grid)
	{
		bool visited[200][200];
		bool mem[200][200]={false};
	
		m = grid.size();
		n = grid[0].size();

		vector<vector<int>> res;

		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				bool i_j_is_true = false;
				if (mem[i][j] == true ||
					i == 0 && j == (n - 1) ||
					i == (m - 1) && j == 0)
					i_j_is_true = true;

				if (!i_j_is_true)
				{

					memset(visited, false, sizeof(visited)); 
					auto ans = dfs(grid,mem,visited,i, j);
					if (ans.first && ans.second)
						i_j_is_true = true;
					
				}
				if (i_j_is_true)
				{
					vector<int> _ = {i, j};
					res.push_back(_);
				}
			}
		}
		return res;
	}
	pair<bool, bool> dfs(vector<vector<int>> &grid,bool mem[200][200],bool visited[200][200],int r, int c)
	{
		bool pacific = false;
		if (r == 0 || c == 0)
			pacific = true;
		bool atlantic = false;
		if (r == m - 1 || c == n - 1)
			atlantic = true;
		if (pacific && atlantic)
		{
			mem[r][c] = true;
			return {pacific, atlantic};
		}

		visited[r][c] = true;

		vector<pair<int, int>> nexts = {{r - 1, c}, {r, c - 1}, {r + 1, c}, {r, c + 1}};
		for (auto p : nexts)
		{
			if ( !(p.first < 0 || p.second < 0 || p.first >= m || p.second >= n) && !visited[p.first][p.second] && grid[p.first][p.second] <= grid[r][c])
			{
				auto ans = dfs(grid,mem,visited,p.first, p.second);
				if (ans.first)
					pacific = true;
				if (ans.second)
					atlantic = true;
			}
		}
		if (pacific && atlantic)
			mem[r][c] = true;
		return {pacific, atlantic};
	}
	
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<vector<int>> heights = {{1, 2, 2, 3, 5}, {3, 2, 3, 4, 4}, {2, 4, 5, 3, 1}, {6, 7, 1, 4, 5}, {5, 1, 1, 2, 4}};
	auto res = s->pacificAtlantic(heights);
	vector_utils::print_2dvector(res);
	/*
	0       4
	1       3
	1       4
	2       2
	3       0
	3       1
	4       0
	*/
	return 0;
}
