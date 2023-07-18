#include <stdio.h>


void print(int n)
{
	printf("%d\n", n);
	--n;
	if (n > 0)
		print(n);
}

int main(void)
{
	print(4);
	return (0);
}
