#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - a number to insert in a singly-linked list
 * @head: pointer to head of linked list
 * @number: number to insert
 * Return: NULL if function fails, otherwise pointer to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;/*current node*/
	listint_t *new_node;/*new node tobe inserted*/

	new_node = malloc(sizeof(listint_t));/*allocate memory for new node*/
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;/*set the n of the new node*/

	/*if list is empty or th first nod's n is greter than or equl to new nmber*/
	if (current == NULL || current->n >= number)
	{
		new_node->next = current;/*new node points to the current node*/
		*head = new_node;/*update the head pointer to the new node*/
		return (new_node);
	}

	/*traverse the list to find the appropriate position to insert the new node*/
	while (current && current->next && current->next->n < number)
		current = current->next;

	new_node->next = current->next;/*new node points to the next node*/
	current->next = new_node;/*current node points to the new node*/

	return (new_node);/*return the new node*/
}
