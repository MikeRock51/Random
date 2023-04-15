#include <stdio.h>


int check_prime(int n, int dec)
{
	if (dec == 1)
		return (1);
	if (n % dec == 0)
		return (0);

	return (check_prime(n, dec - 1));
}

int is_prime_number(int n)
{
	if (n < 2)
		return (0);

	return (check_prime(n, n - 1));
}


/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    int r;

    r = is_prime_number(1);
    printf("%d\n", r);
    r = is_prime_number(1024);
    printf("%d\n", r);
    r = is_prime_number(16);
    printf("%d\n", r);
    r = is_prime_number(17);
    printf("%d\n", r);
    r = is_prime_number(25);
    printf("%d\n", r);
    r = is_prime_number(-1);
    printf("%d\n", r);
    r = is_prime_number(113);
    printf("%d\n", r);
    r = is_prime_number(7919);
    printf("%d\n", r);
    return (0);
}
