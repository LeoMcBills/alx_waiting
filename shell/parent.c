#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(void)
{
	pid_t ppid;

        ppid = getppid();

	printf("The parent id of this child process is %u\n", ppid);
	return (0);
}
