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
    int reverse(int x)
    {
        /*idea:int has range –2147483648 through 2147483647*/

        /*1. obtain the digits*/
        vector<int> digits;

  
        int x_copy=x;
        while (x_copy != 0)
        {
            int cur_digit=x_copy % 10;
            if (cur_digit<0)cur_digit*=-1;
            digits.push_back(cur_digit);
            x_copy /= 10;
        }

        /*2. check if the reversed int is too large when the digits vector have the same number of digits as int_max*/

        bool prev_digit_is_just_big_enough = false;
        if (digits.size() == 10)
        {

            int int_max_first_9[] = {2, 1, 4, 7, 4, 8, 3, 6, 4, 8};
            int i = 0;
            for (auto d : digits)
            {
                if (d > int_max_first_9[i])
                {
                    return 0;
                }
                else if (d == int_max_first_9[i])
                    prev_digit_is_just_big_enough = true;
                else
                    break;

                i += 1;

                /*the last digit check*/
                if (i == 9)
                {
                    if (x < 0)
                    {
                        if (digits[9] > 8)
                            return 0;
                    }
                    else
                    {
                        if (digits[9] > 7)
                            return 0;
                    }
                }
            }
        }

        /*3. create the answer*/
        std::string num_str;
        for (auto d : digits)
        {
            num_str += std::to_string(d);
        }
        int res = std::atoi(num_str.c_str());
        if (x < 0)
            res *= -1;
        return res;
    }
};
/**copy to here**/

int main()
{
    Solution *s = new Solution();
    int test_case = 0, start_from = 0;



    /*case 1*/
    if (test_case >= start_from)
    {
        auto res = s->reverse(123);

        cout << res << endl;
        // 321
    }
    test_case += 1;

    /*case 2*/
    if (test_case >= start_from)
    {
        auto res = s->reverse(2147483647);

        cout << res << endl;
        //
    }
    test_case += 1;

    /*case 3*/
    if (test_case >= start_from)
    {
        auto res = s->reverse(-2147483648);

        cout << res << endl;
        //
    }
    test_case += 1;

    /*case 3*/
    if (test_case >= start_from)
    {
        auto res = s->reverse(2147483640);

        cout << res << endl;
        //
    }
    test_case += 1;

    /*case 4*/

    if (test_case >= start_from)
    {
        auto res = s->reverse(-2147483412);

        cout << res << endl;
        //
    }
    test_case += 1;
    
    /*case 4*/

    if (test_case >= start_from)
    {
        auto res = s->reverse(-123);

        cout << res << endl;
        //-321
    }
    test_case += 1;
    return 0;
}
