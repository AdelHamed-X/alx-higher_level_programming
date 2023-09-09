#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *tmp = *head;
    listint_t *new = NULL;

    new = malloc(sizeof(listint_t));
    while (tmp)
    {
        tmp = tmp->next;

        if (tmp->next->n > number)
        {
            new->n = number;
            new->next = tmp->next;

            tmp->next = new;
            return (new);
        }
    }
    return NULL;
}
