#include <stdlib.h>
#include <stdio.h>

// Flips a tree recursively

//      8           8
//    7   9   =>  9   7
//   5 4 3 5     5 3 4 5

struct Node {
	struct Node *left;
	struct Node *right;
	int val;
};


void flipTree(struct Node *n)
{
	struct Node *tmp = n->left;
	n->left = n->right;
	n->right = tmp;
	if (n->left != NULL) {
		flipTree(n->left);
	}
	if (n->right != NULL) {
		flipTree(n->right);
	}
}

void printTree(struct Node *n, int spaces)
{
	if (n != NULL) {
	 	printTree(n->left, spaces+2);
	 	for (int i = 0; i <= spaces; i++)
	 		printf(" ");
	 	printf("%d\n", n->val);
	 	printTree(n->right, spaces+2);
	}
}

int main()
{
	struct Node *n = calloc(1, sizeof(struct Node));
	struct Node *n1 = calloc(1, sizeof(struct Node));
	struct Node *n2 = calloc(1, sizeof(struct Node));
	struct Node *n3 = calloc(1, sizeof(struct Node));
	struct Node *n4 = calloc(1, sizeof(struct Node));
	struct Node *n5 = calloc(1, sizeof(struct Node));
	struct Node *n6 = calloc(1, sizeof(struct Node));

	n->val = 8;
	n1->val = 7;
	n2->val = 9;


	n->left = n1;
	n->right = n2;

	n3->val = 5;
	n4->val = 4;

	n1->left = n3;
	n1->right = n4;

	n5->val = 3;
	n6->val = 5;

	n2->left = n5;
	n2->right = n6;


	printTree(n, 0);
	flipTree(n);
	printf("\n");
	printTree(n, 0);


}