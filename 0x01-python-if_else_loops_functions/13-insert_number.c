#include "lists.h"

/**
 * insert_node - function that inserts a number to a sorted singly-linked list.
 * @head: pointer to the head of the linked list.
 * @number:  number to be inserted.
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next && current->next->n < number)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}

