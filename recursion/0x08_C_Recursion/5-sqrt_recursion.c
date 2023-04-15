#include <stdio.h>


int get_sqrt(int n, int sq)
{
	/**
	 * Check if the value of sq is greater than n / 2
	 * Or the value of n is less than sq squared.
	 * If true, n does not have a natural square root
	 */
	if (sq > n / 2 || n < sq * sq)
		return (-1);
	/* Check if the current value of sq is the square root of n*/
	if (sq * sq == n)
		return (sq);

	/* Recursively check the return value of sq + 1 against n until a base case is reached */
	return get_sqrt(n, sq + 1);
}

int _sqrt_recursion(int n)
{
	/* Check if n is 0 or 1 in which case, n is the square root of itself */
	if (n == 0 || n == 1)
		return (n);

	return (get_sqrt(n, 0));
}

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    int r;

    r = _sqrt_recursion(1);
    printf("%d\n", r);
    r = _sqrt_recursion(1024);
    printf("%d\n", r);
    r = _sqrt_recursion(16);
    printf("%d\n", r);
    r = _sqrt_recursion(17);
    printf("%d\n", r);
    r = _sqrt_recursion(25);
    printf("%d\n", r);
    r = _sqrt_recursion(-1);
    printf("%d\n", r);
    return (0);
}
