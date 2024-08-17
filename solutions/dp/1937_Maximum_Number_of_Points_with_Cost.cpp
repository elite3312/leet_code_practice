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
class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        int m = points.size(), n = points[0].size();
        vector<long long> prev(points[0].begin(), points[0].end());
        //prev[j] is the best value that comes from making best selections up to
        // the previous row with col j selected

        for (int i = 1; i < m; ++i) {
            vector<long long> left_max(n), right_max(n);//running maximums

            left_max[0] = prev[0];
            for (int j = 1; j < n; ++j)
                                    //max(take the best value to the left of j, prev[j])
                left_max[j] = max(left_max[j-1] - 1, prev[j]);

            right_max[n-1] = prev[n-1];
            for (int j = n-2; j >= 0; --j)
                right_max[j] = max(right_max[j+1] - 1, prev[j]);

            for (int j = 0; j < n; ++j)
                prev[j] = points[i][j] + max(left_max[j], right_max[j]);
        }

        return *max_element(prev.begin(), prev.end());
    }
    long long maxPoints_0(vector<vector<int>>& points) {
        /*O(n^3)*/
        int m=points.size(),n=points[0].size();
        vector<vector<long>>dp(m, vector<long>(n, 0));

        for (int i =0;i<m;++i){
            if (i==0){
                for(int j=0;j<n;++j)dp[i][j]=points[i][j];
                continue;
            }
            for(int j=0;j<n;++j)
                for (int k=0;k<n;++k)
                    dp[i][j]=max(dp[i][j],points[i][j]+dp[i-1][k]-abs(j-k));
            
        }
        return *max_element(dp[m-1].begin(),dp[m-1].end());
    }
};
/**copy to here**/
int main()
{
    Solution *s = new Solution();
    vector<vector<int>> a = {{1,5},{2,3},{4,2}};
    cout<<s->maxPoints(a);//11
    /*
    1 5
      v
    2 3
      v
    4 2
    v
    */

    return 0;
}
