#include "utils/linked_list.hpp"
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace linked_list;
using namespace std;


class Solution_0 {
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

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* long_l, *short_l,*head,*prev;
        if (getCount(l1)>getCount(l2)){
            head=long_l=l1;
            short_l=l2;
        }
        else{
            head=long_l=l2;
            short_l=l1;
        }
        int overflow=0,cur_sum;
        while (short_l){
            cur_sum=short_l->val+long_l->val+overflow;
            if (cur_sum>=10){
                long_l->val =cur_sum-10;
                overflow=1;
            }
            else{
                long_l->val =cur_sum;
                overflow=0;
            }
            //step
            prev=long_l;
            long_l=long_l->next;
            short_l= short_l->next;
        }
        while(long_l){
            cur_sum=long_l->val+overflow;
            if (cur_sum>=10){
                long_l->val =cur_sum-10;
                overflow=1;
            }
            else{
                long_l->val =cur_sum;
                overflow=0;
                break;
            }
            //step
            prev=long_l;
            long_l=long_l->next;
        }
        if (overflow){
            prev->next=new ListNode(1);
        }
        return head;
    }
  
};
int main (){
    Solution *s=new Solution();
    ListNode *head1,*head2,*res;
    head1=new ListNode(2);
    head1->next=new ListNode(4);
    head1->next->next=new ListNode(3);

    head2=new ListNode(5);
    head2->next=new ListNode(6);
    head2->next->next=new ListNode(4);
    //342+465=807
    res=s->addTwoNumbers(head1,head2);
    print_list(res);

    head1=new ListNode(5);
    head2=new ListNode(5);

    res=s->addTwoNumbers(head1,head2);
    print_list(res);
    //01
    return 0;
}
/*idea:
start from last digit
do:
    cursum=l1->val+l2->val+overflow
    if cursum>=10:overflow=1

when one list reachers end
do:
    cursum=l->valoverflow
    if cursum>=10:overflow=1
if overflow is still 1:
    add 1 node(1)
*/
