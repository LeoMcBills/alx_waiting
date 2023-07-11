#include "main.h"

void addNode(struct node *head, struct node *next, int data)
{
    next = malloc(sizeof(struct node));
    head->link = next;
    next->data = data;
    next->link = NULL;
}
