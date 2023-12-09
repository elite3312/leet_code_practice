#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        int r = grid.size(), c = grid[0].size();
        unordered_map<int, int> parent;
        unordered_map<int, int> size;
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
            {
                if (grid[i][j])
                {
                    parent[i * c + j] = i * c + j;
                    size[i * c + j] = 1;
                }
                else
                {
                    parent[i * c + j] = -1;
                    size[i * c + j] = 0;
                }
            }
        int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        bool has_one = false;
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
            {
                if (grid[i][j])
                {
                    has_one = true;
                    for (int k = 0; k < 4; k++)
                    {
                        int ni=i + dirs[k][0],nj=j + dirs[k][1];
                        if (valid_rc ( ni,nj ,r,c)&& grid[ ni][nj])
                            merge(i*c+j,ni*c+nj,size,parent);
                    }
                }
            }
        if (!has_one) return 0;
        int res=0;
        for (int i=0;i<r*c;i++)
            res=max(res,size[i]);
        return res;
    }
    int find(int x, unordered_map<int, int> &parent)
    {
        if (parent[x] == x)
            return x;
        else
            return parent[x] = find(parent[x], parent);
    }
    void merge(int a, int b, unordered_map<int, int> &size, unordered_map<int, int> &parent)
    {
        a = find(a, parent);
        b = find(b, parent);
        if (a != b)
        {
            if (size[a] >= size[b])
            {
                parent[b] = a;
                size[a] += size[b];
                size[b] = 0;
            }
            else
            {
                parent[a] = b;
                size[b] += size[a];
                size[a] = 0;
            }
        }
    }

    bool valid_rc(int i, int j, int r, int c)
    {
        return (i < 0 || j < 0 || i >= r || j >= c) ? false : true;
    }
};
int main()
{
    Solution *s = new Solution();
    vector<vector<int>> input1 = 
        {
        {0,0,1}, 
        {1,1,1}};

    //vector<int> input2 = {11, 6249};

    vector<int> res = {4};

    int n = res.size();
    for (int i = 0; i < n; i++)
    {
        int out = s->maxAreaOfIsland(input1 );
        if (res[i] != out)
            cout << "case " << i << " failed";
    }
    return 0;
}