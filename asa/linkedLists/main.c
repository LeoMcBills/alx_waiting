#include "main.h"

int main(void)
{
   printf("Hello Leo the greatest.\n");
   
   struct node *head = NULL;

   head = malloc(sizeof(struct node));

   head->data = 12;
   head->link = NULL;
   printf("The head data contains %d\n", head->data);
   
   struct node *next;
  
   next = malloc(sizeof(struct node));
   head->link = next;
   next->data = 14;
   next->link = NULL;

   printf("The value of next data is %d\n", next->data);
   printf("%p is what is in head->link.\n", head->link);

   return (0);
}
