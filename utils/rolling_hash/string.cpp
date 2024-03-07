//【例2】對字串進行hash
#include <iostream>
using namespace std;
const int mul = 37, mod = 1e9 + 7;
 
int main() {
    string s = "abcde";
    long long Hash = 0;
    for (auto i: s){
        Hash *= mul;
        Hash += (int) i; //轉成 ASCII code
        Hash %= mod;
        cout << Hash << ' ';
    }
    return 0;
}