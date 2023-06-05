#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to be checked
 * Return: 1 if cycle has been found, 0 if no cycle found
*/

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0); /* empty list or single node, no cycle*/
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1); /*cycle found*/
	}
	return (0); /*no cycle found*/
}
