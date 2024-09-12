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
    int countConsistentStrings(string allowed, vector<string>& words) {
        map<char,bool>m;
        for (auto c:allowed)m[c]=true;
        auto res=0;
        for (auto w:words){
            bool is_valid=true;
            for(auto c:w)
                if (m[c]==false){
                    is_valid=false;
                    break;
                }
            if (is_valid)res+=1;
        }
        return res;
    }
};
/**copy to here**/

int main()
{
    Solution *s = new Solution();
    int test_case = 0, start_from = 0;


    vector<string> words;
    string allowed;

    /*case 1*/
    if (test_case>=start_from)
        {
            words={"ad","bd","aaab","baa","badab"};
            allowed="ab";
            cout<<s->countConsistentStrings(allowed,words)<<endl<<2;
        
        }
    
    test_case += 1;
    
    

    return 0;
}
