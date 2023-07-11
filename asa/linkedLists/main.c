#include "main.h"

int main(void)
{
   struct node *head = NULL;

   head = malloc(sizeof(struct node));
   head->data = 12;
   head->link = NULL;

   struct node *next;
   addNode(head, next, 14);
   printf("The value of head data is %d\n", head->data);
   printf("The value of next data is %d\n", next->data);
   return (0);
}
