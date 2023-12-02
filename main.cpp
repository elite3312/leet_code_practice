#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {}; // No solution found
    }
};
int main (){
    Solution *s=new Solution();
    vector<int> v;
    v.push_back(1);
    
    v.push_back(4);
    s->twoSum(v,5);
    return 0;
}