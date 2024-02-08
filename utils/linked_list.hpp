#ifndef LINKED_LIST_HPP
#define LINKED_LIST_HPP
namespace linked_list
{
    struct ListNode
    {
        int val;
        ListNode *next;
        ListNode() : val(0), next(0) {}
        ListNode(int x) : val(x), next(0) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}
    };
    void print_list(ListNode *head);
    void  reverse(ListNode **head);
    int getCount(ListNode * head);
}
#endif // LINKED_LIST_HPP