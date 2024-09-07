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

// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    bool isSubPath(ListNode *head, TreeNode *root)
    {
        if (root==NULL)return false;

        if(check(head,root))return true;
        if (isSubPath(head,root->left))return true;
        if (isSubPath(head,root->right))return true;
        return false;
    }
    bool check(ListNode *listCur, TreeNode *treeCur){
        if (treeCur==NULL)return false;

        if (treeCur->val!=listCur->val)return false;
        else{
            if (listCur->next==NULL)return true;
            else{
                if (check(listCur->next,treeCur->left))return true;
                if (check(listCur->next,treeCur->right))return true;
                return false;
            }
        }

    }
    
};

/**copy to here**/
int main()
{
    Solution *s = new Solution();

    vector<int> v;
    TreeNode *root;
    ListNode *cur;
    ListNode *head;

    int test_case = 0, start_from = 0;
    /*case 1*/
    /*
          1
        /   \
       4      4
        \    /
        2    2
        /    /\
       1    6  8
              / \
              1 3
    */
    v = {4, 2, 8};
    cur = new ListNode(0);
    head = cur;
    for (auto e : v)
    {
        cur->next = new ListNode(e);
        cur = cur->next;
    }
    head = head->next;

    root = new TreeNode(1);

    root->left = new TreeNode(4);
    root->right = new TreeNode(4);

    root->left->right = new TreeNode(2);
    root->left->right->left = new TreeNode(1);

    root->right->left = new TreeNode(2);
    root->right->left->left = new TreeNode(6);
    root->right->left->right = new TreeNode(8);

    root->right->left->right->left = new TreeNode(1);
    root->right->left->right->right = new TreeNode(3);
    if (test_case >= start_from)
        cout << s->isSubPath(head, root); // 1
    test_case += 1;
    /*case 2*/
    /*
    v={1,10}
    tree={
       1
        \
         1
        / \
       10  1
       /
      9
    }
    */
    v = {1, 10};
    cur = new ListNode(0);
    head = cur;
    for (auto e : v)
    {
        cur->next = new ListNode(e);
        cur = cur->next;
    }
    head = head->next;
    root = new TreeNode(1);
    root->right = new TreeNode(1);
    root->right->left = new TreeNode(10);
    root->right->right = new TreeNode(1);
    root->right->left->left = new TreeNode(9);
    if (test_case >= start_from)
        cout << s->isSubPath(head, root); // 1
    test_case += 1;
    /*case 3*/
    /*
    v={2,2,1}
    tree={
       2
        \
         2
          \
           2
            \
             1
    }
    */
    v = {2, 2, 1};
    cur = new ListNode(0);
    head = cur;
    for (auto e : v)
    {
        cur->next = new ListNode(e);
        cur = cur->next;
    }
    head = head->next;
    root = new TreeNode(2);
    root->right = new TreeNode(2);
    root->right->right = new TreeNode(2);
    root->right->right->right = new TreeNode(1);
    if (test_case >= start_from)
        cout << s->isSubPath(head, root); // 1
    test_case += 1;

    /*case 4*/
    /*
    v={4,2,8}
    tree={
            4
         /    \
        2      2
         \     /
          2    2
         /    / \
        1    6   2
                / \
                1  8
    }
    */
    v = {4, 2, 8};
    cur = new ListNode(-1);
    head = cur;
    for (auto e : v)
    {
        cur->next = new ListNode(e);
        cur = cur->next;
    }
    head = head->next;
    root = new TreeNode(4);
    root->right = new TreeNode(2);
    root->left = new TreeNode(2);

    root->left->right = new TreeNode(2);
    root->right->left = new TreeNode(2);

    root->left->right->left = new TreeNode(1);
    root->right->left->left = new TreeNode(6);
    root->right->left->right = new TreeNode(2);

    root->right->left->right->left = new TreeNode(1);
    root->right->left->right->left = new TreeNode(8);

    if (test_case >= start_from)
        cout << s->isSubPath(head, root); // 0
    test_case += 1;
    return 0;
}
