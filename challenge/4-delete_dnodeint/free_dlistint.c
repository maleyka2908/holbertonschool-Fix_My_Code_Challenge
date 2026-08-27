#include "lists.h"
#include <stdlib.h>

void free_dlistint(dlistint_t *head)
{
    dlistint_t *tmp;
    while (head != NULL)
    {
        tmp = head->next;
        free(head);
        head = tmp;
    }
}
