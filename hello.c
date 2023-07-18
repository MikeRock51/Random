#include <stdio.h>


int sum(int n1, int n2);

int main(void)
{
	printf("Hello Ekene");
	printf("%d\n", sum(10, 10));
	return (0);
}

int sum(int n1, int n2)
{
	return (n1 + n2);
}
