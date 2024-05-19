#include <stdlib.h>

typedef struct list
{
    int val;
    struct list *next;
} list;

// Search a value
list *search_list(list *l, int x)
{
    if (l == NULL)
    {
        return NULL;
    }

    if (l->val == x)
    {
        return l;
    }

    return search_list(l->next, x);
}

// Insert a new node
void insert_list(list **l, int x)
{
    list *p;
    p = malloc(sizeof(list));
    p->val = x;
    p->next = *l;
    *l = p;
}

// Helper for 'delete' - find the node that comes before the node to be deleted
list *predecessor(list *l, int x)
{
    if ((l == NULL) || (l->next == NULL))
    {
        printf("Error: predecessor sought on null list.\n");
        return NULL;
    }

    if ((l->next)->val == x)
    {
        return l;
    }

    return predecessor(l->next, x);
}

// Delete a node
void delete(list **l, int x)
{
    list *p;
    list *pred;

    p = search_list(*l, x);
    if (p == NULL)
    {
        printf("Error: item not found on list.\n");
        return;
    }

    pred = predecessor(*l, x);
    if (pred == NULL)
    {
        *l = p->next;
    }
    else
    {
        pred->next = p->next;
    }

    free(p);
}
