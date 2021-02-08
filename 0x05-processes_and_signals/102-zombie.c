#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
* main - program that creates 5 zombie processes.
* @
* Return: 0 for success
*/

int main(void)
{
	int zomb = 1;
	pid_t newprocess;

	while (1)
	{
		sleep(2);

		while (zomb <= 5)
		{
			newprocess = fork();
			if (newprocess == 0)
			{
				printf("Zombie process created, PID: %d\n", getpid());
				exit(0);
			}
			zomb++;
		}
	}
	return (0);
}
