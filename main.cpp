#include "utils/linked_list.hpp"
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace linked_list;
using namespace std;


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int list_sum= list_2_int(l1)+list_2_int(l2);
        return int_2_list(list_sum);
    }
    ListNode* int_2_list(int i){
        ListNode*cur=NULL;

        int curr_num=i %10;
        cur=new ListNode(curr_num);
        ListNode*head=cur;
        i /=10;
        while(i>0){
            int curr_num=i %10;
            //step
            cur->next=new ListNode(curr_num);
            cur=cur->next;
            i /=10;
        }
        return head;
    }
    int list_2_int(ListNode* l){
        long long num_sum=0;
        ListNode* cur=l;
        int base=1;
        while (cur){
            num_sum+=base*cur->val;
            
            //update state
            base*=10;
            cur=cur->next;
        }
        return num_sum;
    }
};
int main (){
    Solution *s=new Solution();
    ListNode *head1=new ListNode(2);
    head1->next=new ListNode(4);
    head1->next->next=new ListNode(3);

    ListNode *head2=new ListNode(5);
    head2->next=new ListNode(6);
    head2->next->next=new ListNode(4);
    ListNode *res=s->addTwoNumbers(head1,head2);
    //342+465=807
    print_list(res);
    return 0;
}
//C:\msys64\ucrt64\bin\g++.exe -fdiagnostics-color=always -g E:\Mirror\git_repos\coding_inerview\leet_code_practice\main.cpp ./utils/linked_list.cpp -o E:\Mirror\git_repos\coding_inerview\leet_code_practice\main.exe