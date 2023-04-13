#include <stdio.h>

int my_atoi(char *str)
{
    return (str + '0');
}


int main(void)
{
    printf("%d\n", my_atoi("123"));
    return (0);
}
