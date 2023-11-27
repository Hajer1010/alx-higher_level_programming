#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - funftion
 * @list: ptr
 * Return: 1 0
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list, *f = list;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
