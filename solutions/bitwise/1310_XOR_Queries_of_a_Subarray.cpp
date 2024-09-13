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
    /*
    example:
    arr:        011 101 111 010
    xor_prefsum:011 110 001 011

    now what if we want the xor of (2,3)?
    we know that any number xored with itself is 0, 
    so we can xor the xor_prefsum of (0,1) to cancel out the values of (0,1)

    011 ^ 110 = 101, which is xor of (2,3)
    */
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n=arr.size();
        vector<int> xor_prefsum(n,0);
        xor_prefsum[0]=arr[0];
        for ( int i =1 ;i<n;++i){
            xor_prefsum[i]=xor_prefsum[i-1]^arr[i];
        }
        vector<int>res;
        for (auto q:queries){
            if (q[0]==q[1])res.push_back(arr[q[0]]);
            else if (q[0]>0)
                res.push_back(xor_prefsum[q[1]]^xor_prefsum[q[0]-1]);
            else
                res.push_back(xor_prefsum[q[1]]);
        }
        return res;
    }
};
/**copy to here**/

int main()
{
    Solution *s = new Solution();
    int test_case = 0, start_from = 0;


    vector<int> arr;
    vector<vector<int>> queries;

    /*case 1*/
    if (test_case>=start_from)
        {
            arr={3};
            queries={{0,0}};
            auto res=s->xorQueries(arr,queries);
            for (auto e : res){
                cout<<e<<' ';
            }
            cout<<endl;
            //3
        }
    test_case += 1;
    
    /*case 2*/
    if (test_case>=start_from)
        {
            arr={1,3,4,8};
            queries={{0,1},{1,2},{0,3},{3,3}};
            auto res=s->xorQueries(arr,queries);
            for (auto e : res){
                cout<<e<<' ';
            }
            cout<<endl;
            //2 7 14 8
        }
    test_case += 1;
    

    return 0;
}
