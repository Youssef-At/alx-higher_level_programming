#include "lists.h"
/**
* print_dlistint - function that prints all the elements
* @h: the input string to be printed
*
* Description: Function to print all elements in dlistint_t list
* Return: the input number of nodes
*/
size_t print_dlistint(const dlistint_t *h)
{
	int count = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	return (count);
}
