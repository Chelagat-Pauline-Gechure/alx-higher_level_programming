#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if singly-linked list has a cycle.
 * @list: linked list to be checked.
 *
 * Return: 0 if no cycle else 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *slower = list;
	listint_t *faster = list;

	/* Check if list is null or contains only 1 node */
	if (!list || !list->next)
		return (0);

	while (slower->next && faster->next && faster->next->next)
	{
		slower = slower->next;
		faster = faster->next->next;

		if (slower == faster)
			return (1);
	}

	return (0);
}
