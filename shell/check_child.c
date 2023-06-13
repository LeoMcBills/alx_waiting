#include <stdio.h>
#include <unistd.h>

int main(void)
{
		pid_t pid;

		pid = getpid();
		printf("The process id of the child is %u\n", pid);

		return (0);
}
