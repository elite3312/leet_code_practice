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
    int gcd(int a,int b){
        // Everything divides 0 
        if (a == 0) 
            return b; 
        if (b == 0) 
            return a; 
    
        // base case 
        if (a == b) 
            return a; 
    
        // a is greater 
        if (a > b) 
            return gcd(a - b, b); 
        return gcd(a, b - a); 
    }
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* next, *cur=head;
        int _gcd;
        while(cur){
            next=cur->next;

            if (!next)break;

            _gcd=gcd(cur->val,next->val);
            ListNode *tmp=new ListNode(_gcd);//put it on the heap
            cur->next=tmp;
            tmp->next=next;

            cur=next;
        }
        return head;
    }
};
/**copy to here**/

int main()
{
    Solution *s = new Solution();

    vector<int> v1,v2;
    ListNode *head,*head1;

    int test_case = 0, start_from = 0;
    
    

    /*case 1*/
    v1 = {18,6,10,3};
    v2={18,6,6,2,10,1,3};

    head = list_from_vec(v1);
    head1=list_from_vec(v2);
    s->insertGreatestCommonDivisors(head);

    while(head){
        cout<<' '<<head->val;
        head=head->next;
    }
    cout<<endl;
    while(head1){
        cout<<' '<<head1->val;
        head1=head1->next;
    }

    
    test_case += 1;

    return 0;
}
