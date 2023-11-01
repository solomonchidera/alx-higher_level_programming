#include "lists.h"

/**
 * insert_node - short description
 *
 * Description: long description
 *
 * @head: argument_1 description
 * @number: argument_2 description
 *
 * Return: return description
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *previous;
	int count;

	count = 0;
	current = previous = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = *head;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	while (current != NULL)
	{
		count++;
		if (current->n >= number)
		{
			if (count == 1)
				*head = new;
			else
				previous->next = new;
			new->next = current;
			return (new);
		}
		previous = current;
		current = current->next;
	}
	previous->next = new;
	new->next = NULL;
	return (new);
}
