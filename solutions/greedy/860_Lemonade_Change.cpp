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
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        //5, 10, 20
        int cash[21]={0},n=bills.size();
        for (int i=0;i<n;++i){
            if (i==0){
                if (bills[i]!=5)return false;
                else cash[5]+=1;
            }
            else{
                if (bills[i]==5){
                    cash[5]+=1;
                    //return 0
                }
                else if (bills[i]==10){
                    cash[10]+=1;
                    //return 5
                    if  (cash[5]>0)
                        cash[5]-=1;
                    else return false;
                }
                else if (bills[i]==20 ){
                    cash[20]+=1;
                    //return 15
                    if (cash[5]>0 && cash[10]>0){
                        cash[5]-=1;
                        cash[10]-=1;
                    }
                    else if (cash[5]>2){
                        cash[5]-=3;
                    }
                    else return false;
                }
            }
        }
        return true;
    }
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	vector<int> b={5,5,5,10,20};//true
    cout<<s->lemonadeChange(b);
	return 0;
}
