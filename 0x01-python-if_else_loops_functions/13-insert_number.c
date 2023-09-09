#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *tmp = *head;

    while (tmp)
    {
        tmp = tmp->next;

        if (tmp->n > number)
        {

        }
    }
}