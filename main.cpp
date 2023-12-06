#include <iostream>
#include <vector>
#include "utils/TestDriver.hpp"
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n=coins.size();
        return n;
    }
};
int main (){
    Solution *s=new Solution();
    vector<int> v={1,2,5};

    int res=0;
    res=s->coinChange(v,11);
    
    cout<<"ret:"<<res;
    
    return 0;
}