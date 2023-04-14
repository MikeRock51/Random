#include <stdio.h>

void print_alpha(char c)
{
	if (c > 'z')
		return;
	
	putchar(c);
	print_alpha(c + 1);
}

int main()
{
	print_alpha('a');
	putchar('\n');
	return (0);
}
