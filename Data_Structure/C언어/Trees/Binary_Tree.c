#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

typedef int BData;

typedef struct _btreenode {
	BData item;
	struct _btreenode* left_child;
	struct _btreenode* right_child;
}Btreenode;

//int main() {
//	Btreenode* n1 = (Btreenode*)malloc(sizeof(Btreenode));
//	Btreenode* n2 = (Btreenode*)malloc(sizeof(Btreenode));
//	Btreenode* n3 = (Btreenode*)malloc(sizeof(Btreenode));
//
//	n1->item = 10;
//	n1->left_child = n2;
//	n1->right_child = NULL;
//
//	n1->item = 20;
//	n1->left_child = n3;
//	n1->right_child = NULL;
//
//	n1->item = 30;
//	n1->left_child = NULL;
//	n1->right_child = NULL;
//
//	free(n1), free(n2), free(n3);
//	return 0;
//}

Btreenode* createnode(BData item) {
	Btreenode* node = (Btreenode*)malloc(sizeof(Btreenode));
	node->item = item;
	node->left_child = NULL;
	node->right_child = NULL;
	return node;
}

void destorynode(Btreenode* node) {
	free(node);
}

void createleftsubtree(Btreenode* root, Btreenode* left) {
	if (root->left_child != NULL)
		exit(1);
	root->left_child = left;
}

void createrightsubtree(Btreenode* root, Btreenode* right) {
	if (root->right_child != NULL)
		exit(1);
	root->right_child = right;
}

int Nodes(Btreenode* node) {
	int r = 0, l = 0;
	if (node->right_child != NULL)
		r = Nodes(node->right_child);
	if (node->left_child != NULL)
		l = Nodes(node->left_child);
	return 1 + r + l;
}

int Height(Btreenode* node) {
	int r = 0, l = 0;
	if (node->right_child != NULL)
		r = Height(node->right_child);
	if (node->left_child != NULL)
		l = Height(node->left_child);
	return 1 + max(r, l);
}

//int main() {
//	Btreenode* node1 = createnode(10);
//	Btreenode* node2 = createnode(20);
//	Btreenode* node3 = createnode(30);
//	Btreenode* node4 = createnode(40);
//	Btreenode* node5 = createnode(50);
//	Btreenode* node6 = createnode(60);
//
//	createleftsubtree(node1, node2);
//	createrightsubtree(node1, node3);
//
//	createleftsubtree(node2, node4);
//	createrightsubtree(node2, node5);
//	
//	createleftsubtree(node3, node6);
//
//	int num_node = Nodes(node1);
//	int height = Height(node1);
//	printf("number of nodes : %d\n", num_node);
//	printf("height of binary tree : %d\n", height);
//
//	destorynode(node1);
//	destorynode(node2);
//	destorynode(node3);
//	destorynode(node4);
//	destorynode(node5);
//	destorynode(node6);
//	return 0;
//}

#define MAX_STACK 50

typedef enum {
	false, true
}bool;


typedef struct {
	BData items[MAX_STACK];
	int top;
}Stack;


void initstack(Stack* pstack) {
	pstack->top = -1;
}

bool isfull(Stack* pstack) {
	return pstack->top == MAX_STACK - 1;
}

bool isempty(Stack* pstack) {
	return pstack->top == -1;
}

BData peek(Stack* pstack) {
	if (isempty(pstack))
		exit(1);
	return pstack->items[pstack->top];
}

void push(Stack* pstack, BData item) {
	if (isfull(pstack))
		exit(1);
	pstack->items[++(pstack->top)] = item;
}
void pop(Stack* pstack) {
	if (isempty(pstack))
		exit(1);
	--(pstack->top);
}


void rinorder(Btreenode* root) {
	if (root != NULL) {
		rinorder(root->left_child);
		if ((root->item)=='+'|| (root->item) == '-'|| (root->item) == '*'|| (root->item) == '/')
			printf("%c ", root->item);
		else
			printf("%d ", root->item);
		rinorder(root->right_child);
	}
}

void inorder1(Btreenode* root) {
	Stack stack;
	initstack(&stack);
	while (1) {
		while (root) {
			push(&stack, root);
			root = root->left_child;
		}
		root = peek(&stack), pop(&stack);
		if ((root->item) == '+' || (root->item) == '-' || (root->item) == '*' || (root->item) == '/')
			printf("%c ", root->item);
		else
			printf("%d ", root->item);
		root = root->right_child;
	}
}

void inorder2(Btreenode* node) {
	Stack stack;
	initstack(&stack);
	while (1) {
		if (node != NULL) {
			push(&stack, node);
			node = node->left_child;
		}
		else if (!isempty(&stack)) {
			node = peek(&stack), pop(&stack);
			if ((node->item) == '+' || (node->item) == '-' || (node->item) == '*' || (node->item) == '/')
				printf("%c ", node->item);
			else
				printf("%d ", node->item);
			node = node->right_child;
		}
		else
			break;
	}
}


void rpreorder(Btreenode* root) {
	if (root != NULL) {
		printf("%d ", root->item);
		rpreorder(root->left_child);
		rpreorder(root->right_child);
	}
}

void preorder(Btreenode* node) {
	Stack stack;
	initstack(&stack);
	push(&stack, node);
	while (!isempty(&stack)) {
		node = peek(&stack)	, pop(&stack);
		printf("%d ", node->item);
		if (node->right_child) {
			push(&stack, node->right_child);
		}
		if (node->left_child) {
			push(&stack, node->left_child);
		}
	}
}

void rpostorder(Btreenode* root) {
	if (root != NULL) {
		rpostorder(root->left_child);
		rpostorder(root->right_child);
		printf("%d ", root->item);
	}
}

void postorder(Btreenode* node) {
	Stack stack;
	initstack(&stack);
	int ans[50], i = 0;

	while (1) {
		while (node) {
			if (node->right_child)
				push(&stack, node->right_child);
			push(&stack, node->item);

			node = node->left_child;
		}
		node = peek(&stack), pop(&stack);

		if (node->right_child && peek(&stack) == node->right_child) {
			pop(&stack);
			push(&stack, node);
			node = node->right_child;
		}
		else {
			ans[i++] = node->item;
			node = NULL;
		}
		
		if (isempty(&stack)) {
			for (int j = 0; j < i; j++)
				printf("%d ", ans[j]);
		}
	}
}


#define MAX_QUEUE   100

typedef struct {
	int front, rear;
	BData items[MAX_QUEUE];
} Queue;


void initqueue(Queue* p) {
	p->front = p->rear = 0;
}

bool qisempty(Queue* p) {
	return p->front == p->rear;
}

BData qpeek(Queue* p) {
	if (isempty(p))
		exit(1);
	return p->items[p->front];
}

void enqueue(Queue* p, BData item) {
	if (isfull(p))
		exit(1);
	p->items[p->rear] = item;
	p->rear = (p->rear + 1) % MAX_QUEUE;
}

void dequeue(Queue* p) {
	if (isempty(p))
		exit(1);
	p->front = (p->front + 1) % MAX_QUEUE;
}

void levelorder(Btreenode* root) {
	Queue queue;
	if (root == NULL)
		return;
	initqueue(&queue);
	enqueue(&queue, root);
	while (!qisempty(&queue)) {
		root = qpeek(&queue);
		dequeue(&queue);
		printf("%d ", root->item);

		if (root->left_child != NULL)
			enqueue(&queue, root->left_child);
		if (root->right_child != NULL)
			enqueue(&queue, root->right_child);
	}
}

//int main() {
//	Btreenode* node1 = createnode(10);
//	Btreenode* node2 = createnode(20);
//	Btreenode* node3 = createnode(30);
//	Btreenode* node4 = createnode(40);
//	Btreenode* node5 = createnode(50);
//	Btreenode* node6 = createnode(60);
//
//	createleftsubtree(node1, node2);
//	createrightsubtree(node1, node3);
//
//	createleftsubtree(node2, node4);
//	createrightsubtree(node2, node5);
//
//	createleftsubtree(node3, node6);
//
//	//rinorder(node1);
//	//printf("\n");
//	//inorder1(node1);
//	//printf("\n");
//	//inorder2(node1);
//	//printf("\n");
//
//	//rpreorder(node1);
//	//printf("\n");
//	//preorder(node1);
//	//printf("\n");
//
//	//rpostorder(node1);
//	//printf("\n");
//	//postorder(node1);
//	//printf("\n");
//	levelorder(node1);
//
//	destorynode(node1);
//	destorynode(node2);
//	destorynode(node3);
//	destorynode(node4);
//	destorynode(node5);
//	destorynode(node6);
//	return 0;
//}

Btreenode* makeexptree(char* exp, int len) {
	Stack stack;
	Btreenode* node, * right_node, * left_node;
	initstack(&stack);

	for (int i = 0; i < len; i++) {
		if (isdigit(exp[i]))
			node = createnode(exp[i]-'0');
		else {
			right_node = peek(&stack), pop(&stack);
			left_node = peek(&stack), pop(&stack);
			node = createnode(exp[i]);
			createrightsubtree(node, right_node);
			createleftsubtree(node, left_node);
		}
		push(&stack, node);
	}
	return peek(&stack);
}

int calexptree(Btreenode* node) {
	int op1 = 0, op2 = 0;
	if (node == NULL)
		return 0;
	if (node->left_child == NULL && node->right_child == NULL)
		return node->item;
	op1 = calexptree(node->left_child);
	op2 = calexptree(node->right_child);

	switch (node->item)
	{
		case '+':	return op1 + op2;
		case '-':	return op1 - op2;
		case '*':	return op1 * op2;
		case '/':	return op1 / op2;
	}
	return 0;
}

int main() {
	char exp[7] = "34+34*-";
	Btreenode* node = makeexptree(exp, 7);
	inorder2(node);
	printf("\n");
	int cal = calexptree(node);
	printf("%d", cal);
}