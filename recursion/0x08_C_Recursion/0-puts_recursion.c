#include <stdio.h>
#include <string.h>

void _puts_recursion(char *s)
{
	if (strlen(s) < 1)
	{
		putchar('\n');
		return;
	}

	putchar(*(s + 0));
	_puts_recursion(s + 1);
}

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    _puts_recursion("Puts with recursion");
    return (0);
}
