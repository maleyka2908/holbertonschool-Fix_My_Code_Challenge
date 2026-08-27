#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Deletes the node at index of a dlistint_t list.
 * @head: Pointer to the head of the list.
 * @index: Index of the node that should be deleted.
 * Return: 1 if it succeeded, -1 if it failed.
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *saved_head;
	dlistint_t *next_node;
	unsigned int i;

	if (head == NULL || *head == NULL)
		return (-1);

	saved_head = *head;

	if (index == 0)
	{
		*head = (*head)->next;
		if (*head != NULL)
			(*head)->prev = NULL;
		free(saved_head);
		return (1);
	}

	for (i = 0; saved_head != NULL && i < index; i++)
	{
		saved_head = saved_head->next;
	}

	if (saved_head == NULL)
		return (-1);

	next_node = saved_head->next;

	if (saved_head->prev != NULL)
		saved_head->prev->next = next_node;

	if (next_node != NULL)
		next_node->prev = saved_head->prev;

	free(saved_head);

	return (1);
}
