/* 
idea:
push a pair onto stack each time 
pair.val is normal val
pair.cur_min is min val among all val after this push
*/
#include <stdio.h>
#include <stdlib.h>

struct Listnode
{
    int val,cur_min;
    struct Listnode *next;
};
typedef struct
{
    struct Listnode *head;
} MinStack;

MinStack *minStackCreate()
{
    MinStack *M = (MinStack *)malloc(sizeof(MinStack));
    M->head = NULL;
    return M;
}

void minStackPush(MinStack *obj, int val)
{
    /*malloc new node*/
    struct Listnode *new_node = (struct Listnode *)(malloc(sizeof(struct Listnode)));
    new_node->next = NULL;
    

    if (obj->head == NULL)
        new_node->val=new_node->cur_min=val;
    else{
        int cur_min=obj->head->cur_min;
        if (val< cur_min)cur_min=val;
        new_node->val=val;
        new_node->cur_min=cur_min;
    }
    new_node->next=obj->head;
    obj->head = new_node;
}

void minStackPop(MinStack *obj)
{
    if (obj->head == NULL)
        return;

    struct Listnode *temp = obj->head;
    obj->head = obj->head->next;
    free(temp);
}

int minStackTop(MinStack *obj)
{
    if (obj->head != NULL)
        return obj->head->val;
    return -1;
}

int minStackGetMin(MinStack *obj)
{
    if (obj->head != NULL)
        return obj->head->cur_min;
    return -1;
}

void minStackFree(MinStack *obj)
{
    while (obj->head != NULL)
    {
        struct Listnode *temp = obj->head;
        obj->head = obj->head->next;
        free(temp);
    }
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, val);

 * minStackPop(obj);

 * int param_3 = minStackTop(obj);

 * int param_4 = minStackGetMin(obj);

 * minStackFree(obj);
*/
int main()
{
    MinStack *m = minStackCreate();
    int a;

    minStackPush(m, -2);
    minStackPush(m, 0);
    minStackPush(m, -3);

    a = minStackGetMin(m);
    printf("%d", a); //-3

    minStackPop(m);
    a = minStackTop(m);
    printf("%d", a); // 0

    a = minStackGetMin(m);
    printf("%d", a); //-2

    return 0;
}
