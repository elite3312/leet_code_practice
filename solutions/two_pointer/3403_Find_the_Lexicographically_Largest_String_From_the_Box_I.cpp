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
    string lastSubstring(string s) {
        int i = 0, j = 1, n = s.size();
        while (j < n) {
            int k = 0;
            while (j + k < n && s[i + k] == s[j + k]) {
                k++;
            }
            if (j + k < n && s[i + k] < s[j + k]) {
                int t = i;
                i = j;
                j = max(j + 1, t + k + 1);
            } else {
                j = j + k + 1;
            }
        }
        return s.substr(i, n - i);
    }

    string answerString(string word, int numFriends) {
        if (numFriends == 1) {
            return word;
        }
        string last = lastSubstring(word);
        int n = word.size(), m = last.size();
        return last.substr(0, min(m, n - numFriends + 1));
    }
};
class Solution0{
public:
    string answerString(string word, int numFriends) {
        if (numFriends ==1) {
            return word;
        } 
        int max_idx=0,cur_max=-1;
        int n=word.size();
        for (int i=0;i<n;i++){
            if (word[i]>cur_max){
                cur_max=word[i];
                max_idx=i;
            }
        }
        int k=n - numFriends + 1;
        return word.substr(max_idx,k);
    }
    string answerString0(string word, int numFriends) {
     
        int n = word.size();
        /*
        n=1,  return word
        n=2,  return word[:n-1]
        n=3,  return word[:n-2]
        */
        if (numFriends ==1) {
            return word;
        } 
        int k=n - numFriends + 1;

        /*first window*/
        auto res= word.substr(0, k);

        /*sliding window from 1 to n-k*/
        for (int i=1;i+ k<=n; i++) {
            string temp;
            bool bigger=false;
            bool equals=false;
            for (int j = 0; j < k; j++) {
                
                if (word[i+j]>res[j])
                    bigger=true;
                else if (word[i+j]==res[j])
                    equals=true;
                if (equals && word[i+j]<res[j])
                    break;
                
                if (bigger || equals)
                    temp.push_back(word[i+j]);
               
            }
            if (temp.size() == k) {
                res = temp;
            }
        }
        return res;
    }
};
/**copy to here**/

int main()
{
    Solution *s = new Solution();
    int test_case = 0, start_from = 0;


    string a;
    int n=2;

    /*case 1*/
    if (test_case>=start_from)
        {
            a="dbca";
            n=2;
            auto res=s->answerString(a,n);
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
            a="gggg";
            n=4;
            auto res=s->answerString(a,n);
            for (auto e : res){
                cout<<e<<' ';
            }
            cout<<endl;
            //3
        }
    test_case += 1;
    
    /*case 3*/
    if (test_case>=start_from)
        {
            a="gh";
            n=1;
            auto res=s->answerString(a,n);
            for (auto e : res){
                cout<<e<<' ';
            }
            cout<<endl;
            //3
        }
    test_case += 1;

    /*case 4*/
    if (test_case>=start_from)
        {
            a="bif";
            n=2;
            auto res=s->answerString(a,n);
            for (auto e : res){
                cout<<e<<' ';
            }
            cout<<endl;
            //3
        }
    test_case += 1;
    return 0;
}
