#include <stdio.h>
#include <stdarg.h>
#include <unistd.h>


void fn1(char initial, char *name) {
	printf("Hello %c. %s\n", initial, name);
}


int print_string(char *str)
{
    int i = 0;

    if (str == NULL)
        return write(STDOUT_FILENO, "(null)", 6);
    while (str[i])
    {
        putchar(str[i]);
        i++;
    }
    return (i);
}


void variadic(char *restrict format, ...) {
	va_list args;
	va_start(args, format);

	int i = 0;

	while (format[i] != '\0') {
		if (format[i] == '%') {
			print_string("Smile ");
			
		}
		else {
			putchar(format[i]);
		}
		i++;
	}
}


int main() {
	//fn1('E', 7);
	variadic("Hello %Ekene\n");
	return(0);
}
