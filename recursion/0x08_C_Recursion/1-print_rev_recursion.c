#include <stdio.h>
#include <string.h>


void _print_rev_recursion(char *s)
{
	if (strlen(s) < 1)
		return;

	_print_rev_recursion((s + 1));
	putchar(*s);
}


/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    _print_rev_recursion("\nColton Walker");
    return (0);
}
