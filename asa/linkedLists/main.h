#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <stdlib.h>

struct node {
	int data;
	struct node *link;
};

void addNode(struct node *head, struct node *next, int Data);

#endif
