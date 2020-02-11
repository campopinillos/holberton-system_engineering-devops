#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int infinite_while(void);
/**
 * main - Creates 5 zombie processes
 *
 * Return: 0
 */
int main(void)
{
	pid_t zombie;
	int i = 0;

	while (i < 5)
	{
		zombie = fork();
		if (!zombie)
			return(EXIT_SUCCESS);
		printf("Zombie process created, PID: %d\n", zombie);
		i++;
	}
	infinite_while();
	return (EXIT_SUCCESS);
}

/**
 * infinite_while - Infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
