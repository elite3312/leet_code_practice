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
class Solution {
 public:
    int minDistance(string word1, string word2) {
    const int m = word1.length();//first word length
    const int n = word2.length();//second word length
    // dp[i][j] := min # of operations to convert word1[0..i) to word2[0..j)
    //vector<vector<int>> dp(m + 1, vector<int>(n + 1));
	int dp[600][600];
	memset(&dp[0][0],0,sizeof(dp));

    for (int i = 1; i <= m; ++i)
      dp[i][0] = i;

    for (int j = 1; j <= n; ++j)
      dp[0][j] = j;

    for (int i = 1; i <= m; ++i)
      for (int j = 1; j <= n; ++j)
        if (word1[i - 1] == word2[j - 1])//same characters
          dp[i][j] = dp[i - 1][j - 1];//no operation
        else
          dp[i][j] = min({dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]}) + 1;
                             //replace       //delete        //insert
    return dp[m][n];
  }
};
/**copy to here**/
int main()
{
    Solution *s = new Solution();
    cout<<s->minDistance("horse","ros");
    //3
    cout<<s->minDistance("intention","execution");
    //5
    return 0;
}

