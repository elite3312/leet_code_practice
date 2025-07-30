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
    int myAtoi(string s) {
        int sign = 1, result = 0,left=0;

        // Remove leading spaces
        while(s[left]==' ')left++;

        // Check for sign
        if (s[left] == '-' || s[left] == '+') {
            if (s[left] == '-') {
                sign = -1;
            }
            left++;
        }

        // Remove leading zeros
        while(s[left]=='0')left++;

        // find first non-digit character to set as right
        int right=s.size()-1,base=1;
        for (int i=left; i < s.size(); i++) {
            if (s[i]< '0' || s[i] > '9') {
                right=i-1;
                break;
            }
        }
        //2147483646
        if (right - left>9){
            if (sign == 1) return INT_MAX;
            else return INT_MIN;
        }
        else if (right - left == 9) {
            // check for overflow
            if (sign == 1 && s.substr(left, 10) > "2147483647") return INT_MAX;
            else if (sign == -1 && s.substr(left, 10) > "2147483648") return INT_MIN;
        }


        // read from right to left
        while ((right>=left))
        {   
            /*
            if (result<0){
                //overflow
                if (sign == 1) return INT_MAX;
                else return INT_MIN;
            }*/
            result+= (s[right] - '0') * base;
            
            if (base ==1000000000) {
                //overflow
                if (sign == 1) return result;
                else return -result;
            }
            base*=10;
            right--;
        }
        return result * sign;
    }
};
//2147483646
//1000000000
/**copy to here**/

int main()
{
    Solution *s = new Solution();
    int test_case = 0, start_from =0;

    string a ="123";
    /*case 1*/
    if (test_case>=start_from)
        {
            auto res=s->myAtoi(a);
           
            cout<<res<<endl;
            //123
        }
    test_case += 1;
    
    a ="-42";
    /*case 1*/
    if (test_case>=start_from)
        {
            auto res=s->myAtoi(a);
           
            cout<<res<<endl;
            //-42
        }
    test_case += 1;
   
    a ="1337c0d3";
    /*case 1*/
    if (test_case>=start_from)
        {
            auto res=s->myAtoi(a);
           
            cout<<res<<endl;
            //1337
        }
    test_case += 1;

    a ="0-1";
    /*case 1*/
    if (test_case>=start_from)
        {
            auto res=s->myAtoi(a);
           
            cout<<res<<endl;
            //0
        }
    test_case += 1;

    a ="-042";
    /*case 1*/
    if (test_case>=start_from)
        {
            auto res=s->myAtoi(a);
           
            cout<<res<<endl;
            //-42
        }
    test_case += 1;

    
    a ="   -042";
    /*case 1*/
    if (test_case>=start_from)
        {
            auto res=s->myAtoi(a);
           
            cout<<res<<endl;
            //-42
        }
    test_case += 1;

        
    a ="2147483646";
    /*case 1*/
    if (test_case>=start_from)
        {
            auto res=s->myAtoi(a);
           
            cout<<res<<endl;
            //2147483646
        }
    test_case += 1;

    
    a ="-91283472332";
    /*case 1*/
    if (test_case>=start_from)
        {
            auto res=s->myAtoi(a);
           
            cout<<res<<endl;
            //-2147483648
        }
    test_case += 1;
    return 0;
}
