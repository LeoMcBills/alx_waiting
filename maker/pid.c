#include "main.h"

pid_t getit(void)
{
    pid_t childpid;

    childpid = getpid();
    return childpid;
}
