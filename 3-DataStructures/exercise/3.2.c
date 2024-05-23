// Reverse the direction of a singly-linked list

#include <stdlib.h>
#include <stdio.h>

typedef struct list
{
    int val;
    struct list *next;
} list;

list *create_sample_list(int length)
{
    list *l = NULL;

    for (int i = length; i > 0; i--)
    {
        list *node = malloc(sizeof(list));
        node->val = i;
        node->next = l; // insert at head
        l = node;
    }

    return l;
}

void print_list(list *l)
{
    list *node = l;

    while (node != NULL)
    {
        printf("%d->", node->val);
        node = node->next;
    }
    printf("\n");
}

void reverse_list(list **l)
{
    list *node = *l;
    list *reversed_list = NULL;

    while (node != NULL)
    {
        list *next = node->next;
        node->next = reversed_list;
        reversed_list = node;
        node = next;
    }

    *l = reversed_list;
}

int main()
{
    list *l = create_sample_list(5);
    print_list(l); // 1->2->3->4->5->
    reverse_list(&l);
    print_list(l); // 5->4->3->2->1->
}