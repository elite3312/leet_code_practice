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
    int minBitFlips(int start, int goal) {
        int res=0;
        for (int i=0;i<32;++i){
            if (start%2!=goal%2)res++;
            start>>=1;
            goal>>=1;
        }
        return res;
    }
};
/**copy to here**/

int main()
{
    Solution *s = new Solution();

    //vector<int> v1,v2;
    //ListNode *head,*head1;

    int test_case = 0, start_from = 0;
    
    
    int start=10,goal=7;
    /*case 1*/
    if (test_case>=start_from){
        cout<<s->minBitFlips(start,goal)<<' ';
        cout<<3;
    }
    test_case += 1;

    /*case 1*/
    start=4,goal=3;
    if (test_case>=start_from){
        cout<<s->minBitFlips(start,goal)<<' ';
        cout<<3;
    }
    test_case += 1;
    
    

    return 0;
}
