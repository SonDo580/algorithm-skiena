#include <stdlib.h>

typedef struct tree
{
    int val;
    struct tree *parent;
    struct tree *left;
    struct tree *right;
} tree;

tree *search(tree *t, int x)
{
    if (t == NULL)
    {
        return NULL;
    }

    if (t->val == x)
    {
        return t;
    }

    if (x < t->val)
    {
        return search(t->left, x);
    }
    else
    {
        return search(t->right, x);
    }

    // This algorithm runs in O(h) time, where h is the height of the tree
}

tree *find_min(tree *t)
{
    tree *min;

    if (t == NULL)
    {
        return NULL;
    }

    min = t;
    while (min->left != NULL)
    {
        min = min->left;
    }

    return min;
}

tree *find_max(tree *t)
{
    tree *max;

    if (t == NULL)
    {
        return NULL;
    }

    max = t;
    while (max->right != NULL)
    {
        max = max->right;
    }

    return max;
}

void in_order_traverse(tree *t)
{
    if (t != NULL)
    {
        in_order_traverse(t->left);
        printf("%d ", t->val);
        in_order_traverse(t->right);
    }

    // This algorithm runs in O(n) time, where n is the number of nodes
}

void insert(tree **t, int x, tree *parent)
{
    // Find a NULL place and insert

    tree *node;

    if (*t == NULL)
    {
        node = malloc(sizeof(tree));
        node->val = x;
        node->left = NULL;
        node->right = NULL;
        node->parent = parent;
        *t = node;
        return;
    }

    if (x < (*t)->val)
    {
        insert(&((*t)->left), x, *t);
    }
    else
    {
        insert(&((*t)->right), x, *t);
    }

    // Allocating memory for the node and linking it to the tree: O(1)
    // Search: O(h)
}

void delete(tree **t, int x)
{
    if (*t == NULL)
    {
        return;
    }

    if (x < (*t)->val)
    {
        delete (&((*t)->left), x);
        return;
    }

    if (x > (*t)->val)
    {
        delete (&((*t)->right), x);
        return;
    }

    // Leaf node
    if ((*t)->left == NULL && (*t)->right == NULL)
    {
        // Root
        if ((*t)->parent == NULL)
        {
            free(*t);
            *t = NULL;
            return;
        }

        if ((*t)->parent->left == *t)
        {
            (*t)->parent->left = NULL;
        }
        else
        {
            (*t)->parent->right = NULL;
        }

        free(*t);
        return;
    }

    // Has only right child
    if ((*t)->left == NULL && (*t)->right != NULL)
    {
        // Root
        if ((*t)->parent == NULL)
        {
            tree *tmp = *t;
            *t = (*t)->right;
            (*t)->parent = NULL;
            free(tmp);
            return;
        }

        if ((*t)->parent->left == *t)
        {
            (*t)->parent->left = (*t)->right;
        }
        else
        {
            (*t)->parent->right = (*t)->right;
        }

        (*t)->right->parent = (*t)->parent;
        free(*t);
        return;
    }

    // Has only left child
    if ((*t)->right == NULL && (*t)->left != NULL)
    {
        // Root
        if ((*t)->parent == NULL)
        {
            tree *tmp = *t;
            *t = (*t)->left;
            (*t)->parent = NULL;
            free(tmp);
            return;
        }

        if ((*t)->parent->left == *t)
        {
            (*t)->parent->left = (*t)->left;
        }
        else
        {
            (*t)->parent->right = (*t)->left;
        }

        (*t)->left->parent = (*t)->parent;
        free(*t);
        return;
    }

    // Has 2 children
    if ((*t)->left != NULL && (*t)->right != NULL)
    {
        tree *min_node = find_min((*t)->right);
        min_node->parent->left = min_node->right;
        (*t)->val = min_node->val;
        delete (&((*t)->right), min_node->val);
    }

    // Each deletion requires at most 2 search operations: O(h)
    // Plus a constant amount of pointer manipulation: O(1)
}