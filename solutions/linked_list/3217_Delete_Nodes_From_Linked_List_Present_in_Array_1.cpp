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

/* Definition for singly-linked list.*/
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *modifiedList(vector<int> &nums, ListNode *head)
    {
        map<int, bool> m;
        for (auto e : nums)
            m[e] = true;
        
        ListNode *cur = head;
        ListNode *prev = NULL;
        while (cur)
        {
            if (m[cur->val])
            {
                if (cur == head){
                    head = head->next;
                    prev = NULL;
                    cur = head;
                }
                else{
                    delete_node(prev);
                    cur=cur->next;
                }
                
            }
            else{
                    prev=cur;
                    cur=cur->next;
                }
        }
        return head;
    }
    void delete_node(ListNode *prev)
    {
        //deletes the next of prev, thus the deleted node must not be the head
        prev->next = prev->next->next;
    };
};
/**copy to here**/
int main()
{
    Solution *s = new Solution();
    ListNode *cur;
    vector<int> v;

    /*case 4*/
    v = {1, 7, 6, 2, 4};
    vector<ListNode> m = {ListNode(3), ListNode(7), ListNode(1), ListNode(8), ListNode(1)};
    for (int i = 0; i < m.size() - 1; ++i)
        m[i].next = &m[i + 1];
    cur = s->modifiedList(v, &m[0]);
    while (cur)
    {
        cout << cur->val;
        cur = cur->next;
    }
    cout << endl; // 38
    /*case 1*/
    v = {1, 2, 3};
    ListNode h(0), h1(1);
    h.next = &h1;
    cur = s->modifiedList(v, &h);
    while (cur)
    {
        cout << cur->val;
        cur = cur->next;
    }
    cout << endl; // 0

    /*case 2*/
    ListNode h2(1), h3(4);
    h2.next = &h3;
    cur = s->modifiedList(v, &h2);
    while (cur)
    {
        cout << cur->val;
        cur = cur->next;
    }
    cout << endl; // 4

    /*case 3*/
    h3.val = 1;
    ListNode h4(2), h5(3), h6(4), h7(5);
    h3.next = &h4;
    h4.next = &h5;
    h5.next = &h6;
    h6.next = &h7;
    cur = s->modifiedList(v, &h3);
    while (cur)
    {
        cout << cur->val;
        cur = cur->next;
    }
    cout << endl; // 45

    
    return 0;
}
