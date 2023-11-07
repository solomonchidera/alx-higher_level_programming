#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 *
 * Description: function in C that checks if a singly linked list is a
 * palindrome.
 *
 * @head: Pointer to head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int i, count;
	int list_array[2048];

	if (current == NULL)
		return (1);
	for (count = 0; current != NULL; count++, current = current->next)
		;
	if (count == 1)
		return (1);
	current = *head;
	if (count % 2 == 0)
	{
		for (i = 0; i < (count / 2); i++, current = current->next)
			list_array[i] = current->n;
		for (i = i - 1; i >= 0; i--, current = current->next)
			if (list_array[i] != current->n)
				return (0);
	}
	else
	{
		for (i = 0; i <= (count / 2); i++, current = current->next)
			list_array[i] = current->n;
		for (i = i - 2; i >= 0; i--, current = current->next)
			if (list_array[i] != current->n)
				return (0);
	}
	return (1);
}
