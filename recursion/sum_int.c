#include <stdio.h>

unsigned int sum_int(unsigned int value)
{
	unsigned int sum = 0;
	if (value <= 0)
		return (0);

	sum += value % 10;
	return (sum + sum_int(value / 10));
}

int main()
{
	printf("%u\n", sum_int(237));
	printf("%u\n", sum_int(5555));

	return (0);
}
