#include <stdio.h>
#include <stdlib.h>

struct node {
	int data;
	struct node *link;
};

int main(void)
{
	struct node *head = NULL;

	head = malloc(sizeof(struct node));
	head->data = 72;
	head->link = NULL;

	printf("The value stored in head pointer is %d\n", head->data);
	free(head);

	return (0);
}
