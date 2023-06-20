#include "main.h"

int main(void)
{
    pid_t getitpid;

    getitpid = getit();
    printf("The child pid of this process is %u\n", getitpid);

    return (0);

}
