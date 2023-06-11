#include <stddef.h>
#include "lists.h"

/**
 * reverse_listint - reverses a singly linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the head of reversed list
*/

listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head;
	listint_t *next_node, *prev_node = NULL;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev_node;
		prev_node = current;
		current = next_node;
	}
	*head = prev_node;
	return (*head);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of linked list
 * Return: if linked list is a palindrome -1, or -0 if is not
*/
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *reversed_head, *midpoint;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	/*calculate the size of the linked list*/
	while (tmp != NULL)
	{
		size++;
		tmp = tmp->next;
	}
	tmp = *head;
	/*find thr midpoint node*/
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	/*checks if the second half needs to be reversed*/
	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	/*reverse the second half and update the reversed_head pointer*/
	reversed_head = reverse_listint(&tmp);
	midpoint = reversed_head;

	tmp = *head;
	/*compare the first half with the reversed second half*/
	while (reversed_head != NULL)
	{
		if (tmp->n != reversed_head->n)
			return (0);
		tmp = tmp->next;
		reversed_head = reversed_head->next;
	}
	/*reverse the second half again to restore the original list*/
	reverse_listint(&midpoint);
	return (1);
}
