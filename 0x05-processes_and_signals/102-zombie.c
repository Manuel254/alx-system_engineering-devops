#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

/**
 * infinite_while - infinite while loop
 *
 * Return: 0 if success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 *
 * Return: 0 if success
 */
int main(void)
{
	int i = 0;

	while (i < 5)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		i++;
	}
	infinite_while();
	return (0);
}
