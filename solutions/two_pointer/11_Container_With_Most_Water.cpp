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
    int maxArea(vector<int>& height) {
        
        int left = 0, right = height.size() - 1;
        int max_area = 0;

        while (left < right) {
            //the smaller height determines the height of the container
            int current_height = min(height[left], height[right]);
            int current_width = right - left;
            max_area = max(max_area, current_height * current_width);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return max_area;
    }
};
/**copy to here**/

int main()
{
    Solution *s = new Solution();
    int test_case = 0, start_from =0;

    /*case 1*/
    if (test_case>=start_from)
        {
            auto res=0;
            vector<int> height = {1,8,6,2,5,4,8,3,7};
            res = s->maxArea(height);
            cout<<res<<endl;
            //123
        }
    test_case += 1;
    
    return 0;
}
