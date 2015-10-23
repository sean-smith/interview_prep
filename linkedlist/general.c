#include <stdio.h>
#include <stdlib.h>

struct Node {
	struct Node *next;
	int val;
};

typedef struct Node Node;

Node *delete(Node *current, int d)
{
	if (current == NULL) {
		return NULL;
	}
	if (d == current->val) {
		return current->next;
	}
	else {
		Node *n = delete(current->next, d);
		return n;
	}
}


Node *insert(Node *head, int val)
{
	if (head == NULL) {
		Node *n = calloc(1, sizeof(Node));
		n->val = val;
		return n;
	}
	else {
		head->next = insert(head->next, val);
		return head;
	}
}

void printList(Node *c)
{
	if (c != NULL) {
		printf("%d -> ", c->val);
		printList(c->next);
	}
	else
		printf("\n");
}


int main() 
{
	Node *n = calloc(1, sizeof(Node));
	printf("%p\n", n);
	n = insert(n, 5);
	printList(n);
	delete(n, 5);
	printList(n);

	return 1;
}