#include "linked_list.hpp" // header in local directory
#include <stdio.h>


/* Print all the elements in the linked list */
void linked_list::print_list(linked_list::ListNode *head) {
    linked_list::ListNode *current_node = head;
   	while ( current_node != NULL) {
        printf("%d ", current_node->val);
        current_node = current_node->next;
    }
}