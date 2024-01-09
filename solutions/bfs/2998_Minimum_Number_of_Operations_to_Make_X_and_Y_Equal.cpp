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
using namespace binary_tree;
using namespace std;
/**copy from here**/
class Solution
{
public:
	void add_to_q(queue<int>&q,int cur,unordered_map<int,bool>&m){
		if (cur%11==0 && !m[cur / 11])
			q.push(cur / 11);
		if (cur%5==0&& !m[cur / 5])
			q.push(cur / 5);
		if ((cur-1)>0&&!m[cur -1])
			q.push(cur - 1 );
		if ( !m[cur + 1])
			q.push(cur+1);
	}
	int minimumOperationsToMakeEqual(int x, int y)
	{
		if (x == y)
			return 0;
		queue<int> q;
		unordered_map<int,bool>m;
		add_to_q(q,x,m);
		int cur, depth = 1, size;
		while (!q.empty())
		{
			size = q.size();
			for (int i = 0; i < size; i++)
			{
				cur = q.front();
				m[cur]=true;
				q.pop();
				if (cur == y)return depth;
				add_to_q(q,cur,m);
			}
			depth++;
		}
		return -1;
	}
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	int x4 = 12, y4 = 4;
	cout << s->minimumOperationsToMakeEqual(x4, y4)<<endl; // 5
	int x3 = 8, y3 = 1;
	cout << s->minimumOperationsToMakeEqual(x3, y3)<<endl; // 4
	int x2 = 25, y2 = 30;
	cout << s->minimumOperationsToMakeEqual(x2, y2)<<endl; // 5
	int x1 = 54, y1 = 2;
	cout << s->minimumOperationsToMakeEqual(x1, y1)<<endl; // 4
	int x = 26, y = 1;
	cout << s->minimumOperationsToMakeEqual(x, y)<<endl; // 3
	return 0;
}
/*idea
use bfs to traverse paths
the optimal path will always appear first in bfs
*/