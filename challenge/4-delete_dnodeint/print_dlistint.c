#include "lists.h"
#include <stdio.h>

size_t print_dlistint(const dlistint_t *h)
{
    size_t n;
    for (n = 0; h != NULL; n++)
    {
        printf("%d\n", h->n);
        h = h->next;
    }
    return (n);
}
