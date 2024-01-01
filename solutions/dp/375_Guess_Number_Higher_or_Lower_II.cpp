/*custom utils*/
#include "utils/linked_list.hpp"
#include "utils/binary_tree.hpp"
using namespace binary_tree;
/*STLs*/
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
/**copy from here**/
using namespace std;

class Solution
{
public:
    int getMoneyAmount(int n)
    {

        vector<vector<int>> dp(n+1, vector<int>(n+1, -1));
        return getMoneyAmountMem(1, n, dp);
    }
    //recursion
    int min_money(int lower, int upper)
    {
        if (lower >= upper)
            return 0;
        int ans = INT_MAX;
        for (int i = lower; i <= upper; i++)
        {
            ans = min(ans, i + max(min_money(lower, i - 1), min_money(i + 1, upper)));
        }
        return ans;
    }
    //dp
    int getMoneyAmountMem(int start, int end, vector<vector<int>> &dp)
    {
        if (start >= end)
            return 0;
        if (dp[start][end] != -1)
            return dp[start][end];

        int ans = INT_MAX;

        for (int i = start; i <= end; i++)
        {
            ans = min(ans, i + max(getMoneyAmountMem(start, i - 1, dp), getMoneyAmountMem(i + 1, end, dp)));
        }

        dp[start][end] = ans;
        return dp[start][end];
    }
};
/**copy to here**/
int main()
{
    Solution *s = new Solution();
    cout << s->getMoneyAmount(10); // 16
    return 0;
}
/*idea:
use dp to minimum of maximum cost from arr[start] to arr[end]
*/
