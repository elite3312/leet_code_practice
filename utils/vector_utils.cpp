#include "vector_utils.hpp" // header in local directory

#include <vector>
#include<iostream>
using namespace std;
using namespace vector_utils;
/* Print all the elements in the linked list */
void vector_utils::print_2dvector(const vector<vector<int>>&vec) {
    for (auto row:vec){
        for(auto col:row)
            cout<<col<<'\t';
        cout<<endl;
    }
}