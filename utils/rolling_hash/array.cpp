//【例1】對陣列內容進行hash
#include <iostream>
using namespace std;
const int mul = 37, mod = 1e9 + 7;
 
int main() {
    int a[] = {1, 2, 3, 4, 5};
    long long Hash = 0;
    for (auto i: a){
        Hash *= mul;
        Hash += i;
        Hash %= mod;
        cout << Hash << ' ';
    }
    return 0;
}