#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node into a sorted linked list
 * @head: Pointer to the first node.
 * @number: Number to be inserted.
 *
 * Return: Pointer to new node, or NULL if it fails.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head;
	listint_t *fresh_node;

	fresh_node = malloc(sizeof(listint_t));
	if (!fresh_node)
		return (NULL);

	fresh_node->n = number;

	/* When the list is empty or num to be inserted is less than the first number */
	if (*head == NULL || current_node->n >= number)
	{
		fresh_node->next = *head;
		*head = fresh_node;
		return (fresh_node);
	}

	/* When the number to be inserted is within the range of the list */
	while (current_node->next)
	{
		if (current_node->n <= number && current_node->next->n >= number)
		{
			fresh_node->next = current_node->next;
			current_node->next = fresh_node;
			return (fresh_node);
		}
		current_node = current_node->next;
	}

	/* When the number to be inserted is greater than the last number */
	if (!current_node->next)
	{
		fresh_node->next = current_node->next;
		current_node->next = fresh_node;
	}

	return (fresh_node);
}
