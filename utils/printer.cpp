#include "printer.hpp" // header in local directory

#include <vector>
#include<iostream>
using namespace std;
using namespace printer;
/* Print all the elements in the linked list */
void printer::print_2dvector(const vector<vector<int>>&vec) {
    for (auto row:vec){
        for(auto col:row)
            cout<<col<<'\t';
        cout<<endl;
    }
}