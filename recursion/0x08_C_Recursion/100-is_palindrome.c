#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int check_palindrome(char *s)
{
	int i = 0, s_len = strlen(s) - 1;

	while(s[i])
	{
		if (s[i] != s[s_len - i])
			return (0);
		i++;
	}
	return (1);
}

int check_palindrome_recursion(char *str, int start, int end)
{
	if (start >= end)
		return(1);
	if (str[start] != str[end])
		return (0);

	return (check_palindrome_recursion(str, start + 1, end -1));
}

int is_palindrome(char *s)
{
	if (strlen(s) == 0)
		return (1);

	return (check_palindrome_recursion(s, 0, strlen(s) - 1));
}

/* int is_palindrome(char *s)
{
	int i = 0, j = strlen(s) - 1;

	if (strlen(s) == 0)
		return (1);

	while (s[i])
	{
		if (s[i] != s[j])
			return (0);
		i++;
		j--;
	}
	return (1);
}
*/

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    int r;

    r = is_palindrome("level");
    printf("%d\n", r);
    r = is_palindrome("redder");
    printf("%d\n", r);
    r = is_palindrome("test");
    printf("%d\n", r);
    r = is_palindrome("step on no pets");
    printf("%d\n", r);
    return (0);
}
