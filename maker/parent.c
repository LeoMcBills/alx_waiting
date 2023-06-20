#include "parent.h"

pid_t parentid(void)
{
    pid_t getid;

    getid = getppid();
    return getid;
}
