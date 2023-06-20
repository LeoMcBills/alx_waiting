#include "main.h"
#include "parent.h"

int main(void)
{
    pid_t getitpid, getpi;

    getitpid = getit();
    getpi = parentid();

    printf("Process identification checker.\n");
    printf("================================================\n");
    printf("The child pid of this process is %u\n", getitpid);
    printf("The parent pid of this process is %u\n", getpi);
    printf("================================================\n");
    printf("There you go. Thanks for working with us.\n");

    return (0);

}
