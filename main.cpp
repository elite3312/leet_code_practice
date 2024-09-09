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
    int get(ListNode *&head){
        if (head==NULL)return -1;
        int ret=head->val;
        head=head->next;
        return ret;
    }
    vector<vector<int>> spiralMatrix(int m, int n, ListNode *head)
    {
        vector<vector<int>> res(m, vector<int>(n, -1));

        ListNode *cur = head;

        int total = m * n, upperleft_r = 0, upperleft_c = 0, 
        curr_r_size = m, curr_c_size = n,tmp;
        
        while (1)
        {
            for (int j = 0; j < curr_c_size; ++j){
                tmp=get(cur);
                if (tmp!=-1)
                    res[upperleft_r][upperleft_c + j] = tmp;
                else
                    return res;
            }
            for (int i = 1; i < curr_r_size; ++i){
                tmp=get(cur);
                if (tmp!=-1)
                    res[upperleft_r+i][upperleft_c + curr_c_size-1] = tmp;
                else
                    return res;
            }
            for (int j= curr_c_size-2; j >=0 ; --j){
                tmp=get(cur);
                if (tmp!=-1)
                    res[upperleft_r+curr_r_size-1][upperleft_c + j] = tmp;
                else
                    return res;
            }
            for (int i=  curr_r_size-2; i>=1 ; --i){
                tmp=get(cur);
                if (tmp!=-1)
                    res[upperleft_r+i][upperleft_c] = tmp;
                else
                    return res;
            }
            if (cur==NULL)return res;
            curr_r_size-=2;
            curr_c_size-=2;
            upperleft_c+=1;
            upperleft_r+=1;
        }

        return res;
    }
};

/**copy to here**/

int main()
{
    Solution *s = new Solution();

    vector<int> v;
    ListNode *head;
    int m, n;
    int test_case = 0, start_from = 0;
    vector<vector<int>> res;
    /*case 4*/
    /*
    4x5
    xxxx
    x  x
    x  x
    x  x
    xxxx
    */
    v = {0};

    head = list_from_vec(v);

    m = 1;
    n = 1;
    res = s->spiralMatrix(m, n, head);
    print_2d_vec(m, n, res);
    test_case += 1;
    /*case 4*/
    /*
    4x5
    xxxx
    x  x
    x  x
    x  x
    xxxx
    */
    v = {515, 942, 528, 483, 20, 159, 868, 999, 474, 320, 734, 956, 12, 124, 224, 252, 909, 732};

    head = list_from_vec(v);

    m = 4;
    n = 5;
    res = s->spiralMatrix(m, n, head);
    print_2d_vec(m, n, res);
    test_case += 1;
    /*case 1*/

    v = {3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0};
    head = list_from_vec(v);

    m = 3;
    n = 5;
    res = s->spiralMatrix(m, n, head);
    print_2d_vec(m, n, res);
    test_case += 1;

    /*case 2*/
    v = {0, 1, 2};

    head = list_from_vec(v);

    m = 1;
    n = 4;
    res = s->spiralMatrix(m, n, head);
    print_2d_vec(m, n, res);
    test_case += 1;

    /*case 3*/
    v = {8, 24, 5, 21, 10, 11, 11, 12, 6, 17};

    head = list_from_vec(v);

    m = 10;
    n = 1;
    res = s->spiralMatrix(m, n, head);
    print_2d_vec(m, n, res);
    test_case += 1;

    return 0;
}
