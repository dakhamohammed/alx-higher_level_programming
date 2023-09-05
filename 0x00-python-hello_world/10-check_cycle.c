#include "lists.h"

/**
 * check_cycle - function that checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_check = list;

	if (list == NULL)
	{
		return (0);
	}

	while (list && fast_check && fast_check->next)
	{
		list = list->next;
		fast_check = fast_check->next->next;

		if (list == fast_check)
		{
			return (1);
		}
	}

	return (0);
}

