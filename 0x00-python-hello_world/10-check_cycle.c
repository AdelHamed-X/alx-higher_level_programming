#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *iterator = list;
    listint_t *pre_iterator = list;


    while (iterator && iterator->next)
    {
        pre_iterator = pre_iterator->next;
        iterator = iterator->next->next;

        if (iterator == pre_iterator)
        {
            return (1);
        }
    }
    return (0);
}
