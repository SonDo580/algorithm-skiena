// Dynamic Array
// - push - overflow strategy: double the size when array is full
// - pop1 - underflow strategy: cut the size in half when array shrinks to half-full
// - pop2 - better underflow strategy: use a lower threshold, 1/4 instead of 1/2

#include <stdlib.h>
#include <stdio.h>

int *initialize(int max_size)
{
    int *dynamic_arr = malloc(max_size * sizeof(int));
    if (dynamic_arr == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    return dynamic_arr;
}

void push(int **dynamic_arr, int *size, int *max_size, int value)
{
    if (*size == *max_size)
    {
        int *new_array = initialize(*max_size * 2);
        *max_size *= 2;

        for (int i = 0; i < *size; i++)
        {
            new_array[i] = (*dynamic_arr)[i];
        }

        free(*dynamic_arr);
        *dynamic_arr = new_array;
    }

    (*dynamic_arr)[*size] = value;
    (*size)++;
}

int pop1(int **dynamic_arr, int *size, int *max_size)
{
    if (*size == 0)
    {
        fprintf(stderr, "Array is empty\n");
        exit(EXIT_FAILURE);
    }

    int value = (*dynamic_arr)[*size - 1];
    (*size)--;

    if (*size == *max_size / 2)
    {
        int *new_array = initialize(*max_size / 2);
        *max_size /= 2;

        for (int i = 0; i < *size; i++)
        {
            new_array[i] = (*dynamic_arr)[i];
        }

        free(*dynamic_arr);
        *dynamic_arr = new_array;
    }

    return value;
}

int pop2(int **dynamic_arr, int *size, int *max_size)
{
    if (*size == 0)
    {
        fprintf(stderr, "Array is empty\n");
        exit(EXIT_FAILURE);
    }

    int value = (*dynamic_arr)[*size - 1];
    (*size)--;

    if (*size == *max_size / 4)
    {
        int *new_array = initialize(*max_size / 2);
        *max_size /= 2;

        for (int i = 0; i < *size; i++)
        {
            new_array[i] = (*dynamic_arr)[i];
        }

        free(*dynamic_arr);
        *dynamic_arr = new_array;
    }

    return value;
}

void print(int *dynamic_array, int size, int max_size)
{
    printf("size / max_size: %d / %d\n", size, max_size);
    for (int i = 0; i < size; i++)
    {
        printf("%d ", dynamic_array[i]);
    }
    printf("\n");
}

int main()
{
    int max_size = 1;
    int size = 0;
    int *dynamic_arr = initialize(max_size);

    for (int i = 0; i < 10; i++)
    {
        push(&dynamic_arr, &size, &max_size, i);
    }
    print(dynamic_arr, size, max_size);

    for (int i = 0; i < 2; i++)
    {
        pop1(&dynamic_arr, &size, &max_size);
    }
    print(dynamic_arr, size, max_size);

    for (int i = 0; i < 6; i++)
    {
        pop2(&dynamic_arr, &size, &max_size);
    }
    print(dynamic_arr, size, max_size);

    free(dynamic_arr);
}