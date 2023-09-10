#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head;
    listint_t *new = NULL;

    new = malloc(sizeof(listint_t));

    new->n = number;
    if (!new)
        return (NULL);

    if (node->n > number)
    {
        new->next = node;
        *head = new;
        return (new);
    }

    while (node->next->n < number)
    {
        node = node->next;
    }

    new->next = node->next;
    node->next = new;
    return (new);
}
