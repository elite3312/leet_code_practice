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
class Solution
{
public:
    string convert(string s, int numRows)
    {
        /*
        P   A   H   N
        A P L S I I G
        Y   I   R
        =>
        1 5 9
        2468
        3 7

        num rows = 3
        */
        if (numRows==1)return s;
        int n = s.size();
        vector<vector<char>> v(numRows, vector<char>(n, ' '));

        int i=0,j=0;
        bool going_down=true;//otherwise go right up
        for (auto c:s)
        {   
            v[i][j]=c;
            bool changed_dir=false;
            if (going_down){
                i++;
                if (i>=numRows-1){
                    going_down=false;
                    changed_dir=true;
                }
            }
            else if (!changed_dir){
                i--;
                j++;
                if (i==0){
                    going_down=true;
                }
            }
            
        }
        string res;
        for (auto _v:v)
            for (auto c:_v)
                if (c!=' '){
                    res+=c;
                    if (res.size()>=n)return res;
                }
        return res;
    }
};
/**copy to here**/

int main()
{
    Solution *s = new Solution();
    int test_case = 0, start_from = 0;

    vector<int> a = {1, 2};
    vector<int> b = {3, 4};

    /*case 1*/
    if (test_case >= start_from)
    {
        auto res = s->convert("PAYPALISHIRING", 3);

        cout << res << endl;
        // PAHNAPLSIIGYIR
    }
    test_case += 1;

    /*case 2*/
    if (test_case >= start_from)
    {
        auto res = s->convert("PAYPALISHIRING", 4);

        cout << res << endl;
        // PINALSIGYAHRPI
    }
    test_case += 1;
    /*case 3*/
    if (test_case >= start_from)
    {
        auto res = s->convert("a", 1);

        cout << res << endl;
        // a
    }
    test_case += 1;

    /*case 4*/
    if (test_case >= start_from)
    {
        auto res = s->convert("ab", 1);

        cout << res << endl;
        // ab
    }
    test_case += 1;
    return 0;
}
