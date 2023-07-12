#include "main.h"

void addNode(struct node *head, struct node *next, int Data)
{
    next = malloc(sizeof(struct node));
    head->link = next;
    next->data = Data;
    next->link = NULL;
}
