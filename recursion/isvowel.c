#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isvowel(char c)
{
	switch (tolower(c))
	{
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':
			return (1);
		default:
			return (0);
	}
}

int check_vowels(char *str)
{
	if (strlen(str) < 1)
		return (0);
	
	return (isvowel(*(str + 0)) + check_vowels((str + 1)));
}

int main()
{
	printf("%d\n", check_vowels("Barbaric"));

	return (0);
}
