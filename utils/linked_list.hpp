#ifndef LINKED_LIST_HPP
#define LINKED_LIST_HPP
namespace linked_list
{
    struct ListNode
    {
        int val;
        ListNode *next;
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}
    };
    void print_list(ListNode *head);

}
#endif // LINKED_LIST_HPP