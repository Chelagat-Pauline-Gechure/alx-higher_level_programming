#include "lists.h"
#include <stdlib.h>
#include <stdbool.h>

int linked_list_length(listint_t **head);
int check_palindrome_bruteforce(listint_t **head);
int palindrome_reverse_half(listint_t **head);
listint_t *reverse(listint_t *start);

/**
 * is_palindrome - checks if  singly-linked list is a palindrome
 * @head: Pointer to head of list.
 *
 * Return: 0 if its not a palindrome or 1 if it is.
 */

int is_palindrome(listint_t **head)
{
    
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    
    if ((*head)->next->next == NULL)
        return ((*head)->n == (*head)->next->n ? 1 : 0);

    
    if ((*head)->next->next->next == NULL)
        return ((*head)->n == (*head)->next->next->n ? 1 : 0);

   
    return (palindrome_reverse_half(head));
}

/**
 * palindrome_reverse_half - checks if a singly-link list is a palindrome
 * @head: Pointer to head of list.
 *
 * This algorithm uses 2 pointers to track the middle of the list,
 * then reversing the second half and then comparing the respective elements.
 * It has a time complexity of 0(n) since the list is only traversed once.
 *
 * Return: 0 if its not a palindrome or 1 if it is.
 */

int palindrome_reverse_half(listint_t **head)
{
    listint_t *slower = *head;
    listint_t *faster = *head;

    while (faster->next && faster->next->next)
    {
        slower = slower->next;
        faster = faster->next->next;
    }

    slower->next = reverse(slower->next);
    slower = slower->next;
    faster = *head;

    while (slower)
    {
        if (faster->n != slower->n)
            return (false);
        slower = slower->next;
        faster = faster->next;
    }

    return (true);
}

/**
 * check_palindrome_bruteforce - checks if a singly-linked list is a palindrome
 * @head: Pointer to head of list.
 *
 * This algorithm gets the length of the list, then allocates an array
 * of integers where the numbers from the list are copied to.
 *
 * Return: 0 if its not a palindrome or 1 if it is.
 */

int check_palindrome_bruteforce(listint_t **head)
{
    int x, list_length, left_index, right_index;
    int *numbers;
    listint_t *curr = *head;

    list_length = linked_list_length(head);

    
    numbers = malloc(sizeof(int) * list_length);
    if (!numbers)
        return (false);

    
    curr = *head;
    for (x = 0; x < list_length; x++, curr = curr->next)
        numbers[x] = curr->n;

    if ((list_length & 1) == 0)
    { 
        right_index = list_length / 2;
        left_index = right_index - 1;
    }
    else if ((list_length & 1) == 1)
    { 
        right_index = (list_length / 2) + 1;
        left_index = (list_length / 2) - 1;
    }
    for (; left_index >= 0; left_index--, right_index++)
        if (numbers[left_index] != numbers[right_index])
        {
            free(numbers);
            return (false);
        }

    free(numbers);
    return (true);
}

/**
 * linked_list_length - returns the length of a linked list
 * @head: Pointer to head of list.
 *
 * Return: Integer, the length of the list.
 */

int linked_list_length(listint_t **head)
{
    listint_t *curr = *head;
    int list_length = 1;

    while (curr->next)
    { 
        list_length++;
        curr = curr->next;
    }

    return (list_length);
}

/**
 * reverse - reverses a linked-list starting from a specified node
 * @start: Node to start reversing from.
 *
 * Return: Pointer to the first node after list has been reversed.
 */

listint_t *reverse(listint_t *start)
{
    listint_t *next = NULL;
    listint_t *prev = NULL;

    while (start)
    {
        next = start->next;
        start->next = prev;
        prev = start;
        start = next;
    }

    start = prev;
    return (start);
}
