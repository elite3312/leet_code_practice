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


// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
ListNode *list_from_vec(vector<int> v)
{
    ListNode *cur = new ListNode(-1);
    ListNode *head = cur;
    for (auto e : v)
    {
        cur->next = new ListNode(e);
        cur = cur->next;
    }
    head = head->next;
    return head;
}
void print_2d_vec(int m, int n, const vector<vector<int>> &res)
{
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
            printf("%2d", res[i][j]);
        cout << endl;
    }
    cout << endl;
}
/**copy from here**/

class Solution {
public:
    bool isPalindrome(int x) {
        string str = to_string(x);
        int n = str.size();
        for (int i = 0; i < n / 2; ++i) {
            if (str[i] != str[n - 1 - i]) {
                return false;
            }
        }
        return true;
    }
};

/**copy to here**/

int main()
{
    Solution *s = new Solution();
    int test_case = 0, start_from =0;

    /*case 1*/
    if (test_case>=start_from)
        {
            auto res=0;
            int x = 121;
            res = s->isPalindrome(x);
            cout<<res<<endl;
            //123
        }
    test_case += 1;
    
    return 0;
}
