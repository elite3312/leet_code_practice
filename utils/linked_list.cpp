//C:\msys64\ucrt64\bin\g++.exe -fdiagnostics-color=always -g E:\Mirror\git_repos\coding_inerview\leet_code_practice\main.cpp ./utils/linked_list.cpp -o E:\Mirror\git_repos\coding_inerview\leet_code_practice\main.exe
#include "linked_list.hpp" // header in local directory
#include <stdio.h>

using namespace linked_list;
/* Print all the elements in the linked list */
void linked_list::print_list(ListNode *head) {
    ListNode *current_node = head;
   	while ( current_node != NULL) {
        printf("%d ", current_node->val);
        current_node = current_node->next;
    }
}
 void linked_list::reverse(ListNode **head)//the reason for using a double pointer is we need to change the value of *head
    {
        // Initialize current, previous and next pointers
        ListNode* current = *head;
        ListNode *prev = NULL, *next = NULL;
 
        while (current != NULL) {
            // Store next
            next = current->next;
            // Reverse current node's pointer
            current->next = prev;
            // Move pointers one position ahead.
            prev = current;
            current = next;
        }
        *head = prev;
    }
int linked_list::getCount(ListNode * head)
{
    int count = 0; // Initialize count
    ListNode* current = head; // Initialize current
    while (current != NULL) {
        count++;
        current = current->next;
    }
    return count;
}