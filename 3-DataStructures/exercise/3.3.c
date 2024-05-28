// Dynamic Array
// - push - overflow strategy: double the size when array is full
// - pop1 - underflow strategy: cut the size in half when array shrinks to half-full
// - pop2 - better underflow strategy: use a lower threshold, 1/4 instead of 1/2

#include <stdlib.h>
#include <stdio.h>

typedef struct
{
    int size;
    int capacity;
    int *entries;
} DynamicArray;

DynamicArray *initialize(int capacity)
{
    DynamicArray *array = malloc(sizeof(DynamicArray));
    if (array == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    array->entries = malloc(capacity * sizeof(int));
    if (array->entries == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    array->capacity = capacity;
    array->size = 0;
    return array;
}

void push(DynamicArray *array, int value)
{
    if (array->size == array->capacity)
    {
        array->capacity *= 2;
        array->entries = realloc(array->entries, array->capacity * sizeof(int));
        if (array->entries == NULL)
        {
            fprintf(stderr, "Memory allocation failed\n");
            exit(EXIT_FAILURE);
        }
    }

    array->entries[array->size] = value;
    array->size++;
}

int pop1(DynamicArray *array)
{
    if (array->size == 0)
    {
        fprintf(stderr, "Array is empty\n");
        exit(EXIT_FAILURE);
    }

    int value = array->entries[array->size - 1];
    array->size--;

    if (array->size == array->capacity / 2)
    {
        array->capacity /= 2;
        array->entries = realloc(array->entries, array->capacity * sizeof(int));
        if (array->entries == NULL)
        {
            fprintf(stderr, "Memory allocation failed\n");
            exit(EXIT_FAILURE);
        }
    }

    return value;
}

int pop2(DynamicArray *array)
{
    if (array->size == 0)
    {
        fprintf(stderr, "Array is empty\n");
        exit(EXIT_FAILURE);
    }

    int value = array->entries[array->size - 1];
    array->size--;

    if (array->size == array->capacity / 4)
    {
        array->capacity /= 2;
        array->entries = realloc(array->entries, array->capacity * sizeof(int));
        if (array->entries == NULL)
        {
            fprintf(stderr, "Memory allocation failed\n");
            exit(EXIT_FAILURE);
        }
    }

    return value;
}

void print(DynamicArray *array)
{
    printf("size / capacity: %d / %d\n", array->size, array->capacity);
    for (int i = 0; i < array->size; i++)
    {
        printf("%d ", array->entries[i]);
    }
    printf("\n");
}

int main()
{
    DynamicArray *array = initialize(1);

    for (int i = 0; i < 10; i++)
    {
        push(array, i);
    }
    print(array);

    for (int i = 0; i < 2; i++)
    {
        pop1(array);
    }
    print(array);

    for (int i = 0; i < 6; i++)
    {
        pop2(array);
    }
    print(array);

    free(array->entries);
    free(array);
}