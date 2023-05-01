#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, char **argv)
{
	char *name = NULL;
	int num;

	name = malloc(sizeof(char) * 1024);


	printf("who is the best?: ");
	scanf("%s", name);

	printf("How awesome is he?: ");
	scanf("%d", &num);


	while (num >= 0)
	{
		printf("%s is Awesome\n", name);
		num--;
	}

	return (0);
}
