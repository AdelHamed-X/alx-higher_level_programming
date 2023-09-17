#include "lists.h"

/**
 *
 *
 *
 */
int is_palindrome(listint_t **head)
{
    listint_t *node = *head;
    int condition1, node_lentgth = 0, i = 0;

    if (*head == NULL)
        return (1);

    while (node->next)
    {
        node_lentgth++;
        node = node->next;
    }
    int *arr = malloc((node_lentgth + 1) * sizeof(int));
    node = *head;

    while (node)
    {
        arr[i] = node->n;
        i++;
        node = node->next;
    }

    condition1 = (node_lentgth) / 2;
    for (i = 0; i < condition1; i++)
    {
        if (arr[i] != arr[node_lentgth - i])
        {
            free(arr);
            return (0);
        }
        else
            continue;
    }
    free(arr);
    return (1);
}
