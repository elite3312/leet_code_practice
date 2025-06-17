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
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n= nums1.size();
        int m= nums2.size();
        //if (n > m) {
        //    return findMedianSortedArrays(nums2, nums1); // Ensure nums1 is the smaller array
        //}

        //O(n+m)
        bool even=false;
        if ((n+m)%2==0)
            even=true;
        
        int target_idx=(n+m)/2;
   
    
        
        int i=0,j=0,total=0;

        double cur,prev;
        while(1){
            
            if (i>=n){
                cur=nums2[j++];
            }
            else if (j>=m){
                cur=nums1[i++];
            }
            else{
                if (nums1[i]<nums2[j])
                    cur=nums1[i++];
                else
                    cur=nums2[j++];
            }
            total+=1;
            if (total>=(target_idx+1))
                break;
            prev=cur;
        }

        if (!even){
            return cur;
        }
        else{
            return (cur+prev)/2;
        }
    }
};
/**copy to here**/

int main()
{
    Solution *s = new Solution();
    int test_case = 0, start_from = 0;


    vector <int>a={1,2};
    vector <int>b={3,4};

    /*case 1*/
    if (test_case>=start_from)
        {
            auto res=s->findMedianSortedArrays(a,b);
           
            cout<<res<<endl;
            //2.5
        }
    test_case += 1;


    a={1,2};
    b={3};
    if (test_case>=start_from)
        {
            auto res=s->findMedianSortedArrays(a,b);
           
            cout<<res<<endl;
            //2
        }
    test_case += 1;
    return 0;
}
