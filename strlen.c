#include <stdio.h>

int my_strlen(const char *s)
{
	int len = 0;

	while (*s)
	{
		len++;
		s++;
	}
	return len;
}

int main(void)
{
	char *str = "Hello";

	printf("%d\n", my_strlen(str));
}
